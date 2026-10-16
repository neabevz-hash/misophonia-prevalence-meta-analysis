# Prevalence of misophonia: meta-analysis (protocol v1.0, sections 13 and 15-17).
#
# Reads forms/samples.csv and forms/estimates.csv (verified extraction, extraction/finalize.py) and writes the
# results to analysis/results/ and the figures to analysis/figures/. Every pooled analysis uses one estimate per
# sample, chosen by the rules of section 13; the choices are written to results/selection_log.csv.
#
# Run from the repository root:
#   Rscript papers/misophonia-prevalence/analysis/analysis.R [forms_dir] [out_dir]
# Defaults: papers/misophonia-prevalence/forms and papers/misophonia-prevalence/analysis.

suppressPackageStartupMessages({
  library(metafor)
  library(lme4)
  library(clubSandwich)
  library(dplyr)
  library(readr)
  library(ggplot2)
})

args <- commandArgs(trailingOnly = TRUE)
forms_dir <- if (length(args) >= 1) args[1] else "papers/misophonia-prevalence/forms"
out_root <- if (length(args) >= 2) args[2] else "papers/misophonia-prevalence/analysis"
res_dir <- file.path(out_root, "results")
fig_dir <- file.path(out_root, "figures")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)
MIN_K <- 3        # section 15b: a pooled estimate needs at least three independent samples
MIN_K_MOD <- 10   # exploratory moderators are tested only when k >= 10
SELECTION <- "registered"   # section 13 step 2: the recommended (first) Table 1 threshold; 'ordered' is a post hoc check

# ---------------------------------------------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------------------------------------------

num <- function(x) suppressWarnings(as.numeric(gsub(",", "", trimws(as.character(x)))))

samples <- read_csv(file.path(forms_dir, "samples.csv"), col_types = cols(.default = "c"), na = character())
ests <- read_csv(file.path(forms_dir, "estimates.csv"), col_types = cols(.default = "c"), na = character())

samples <- samples |>
  mutate(
    nonclinical = population != "clinical",
    poptype = case_when(
      population == "gp_probability" ~ "probability general population",
      population == "gp_other" ~ "other general population",
      population %in% c("university_students", "medical_students") ~ "university students",
      population == "school_pupils" ~ "school children and adolescents",
      population %in% c("workers", "other_nonclinical") ~ "other non-clinical",
      TRUE ~ "clinical"),
    prob = sampling %in% c("probability", "census"),
    agegrp = case_when(age_group == "children" ~ "children (<13)", age_group == "adolescents" ~ "adolescents (13-17)",
                       age_group == "adults" ~ "adults", TRUE ~ "mixed or NR"),
    contgrp = case_when(continent %in% c("Asia", "Europe", "Americas") ~ continent,
                        continent %in% c("Africa", "Oceania") ~ "other", TRUE ~ NA_character_),   # NR or several countries
    age_mean_n = num(age_mean), pct_female_n = num(pct_female), year_data = num(substr(data_years, 1, 4)),
    journal = pub_status == "journal",
    clin = ifelse(population == "clinical", sub("[ :(].*$", "", clinical_group), NA_character_))   # code before notes

ests <- ests |>
  mutate(cases_n = num(cases), n_n = num(n),
         sub = tolower(trimws(subgroup)),
         poolable = level %in% c("L1", "L2", "L3") & !is.na(cases_n) & !is.na(n_n) & n_n > 0 & cases_n <= n_n &
           cases_n >= 0) |>
  left_join(samples |> select(sample_id, study_id, first_author, year, country, nonclinical, poptype, prob, agegrp,
                              contgrp, clin,
                              age_mean_n, pct_female_n, year_data, journal, topic_disclosed, mode, continent,
                              who_region, income_group, sampling, starts_with("jbi_")),
            by = "sample_id")

whole <- ests |> filter(sub %in% c("all", "total", "whole sample"), poolable)

# ---------------------------------------------------------------------------------------------------------------
# One estimate per sample (section 13)
# ---------------------------------------------------------------------------------------------------------------

# Threshold recommended in Table 1 (first threshold in the L1_rule / L2_rule column, rule G11).
# Thresholds of Table 1 (forms/instrument_thresholds.csv), per instrument and level, in the order of the L1_rule and
# L2_rule columns; the first one is the recommended threshold (rule G11).
ge <- function(x) paste0("((>=|≥)\\s*", x, "\\b|>\\s*", x - 1, "\\b)")
TABLE1 <- list(
  "A-MISO-S L1" = c(ge(5)), "A-MISO-S L2" = c(ge(10), ge(15)),
  "AMISOS-R L1" = c(ge(11)), "AMISOS-R L2" = c(ge(24), ge(21)),
  "MQ L1" = c(paste0("(mss|severity)[^;]*", ge(4)), paste0("symptom[^;]*", ge(14))),
  "MQ L2" = c(paste0("^(?!.*(emotion|e&b)).*(mss|severity|item 18)[^;]*", ge(7)), paste0("total[^;]*", ge(30)),
              paste0("(emotion|e&b)[^;]*", ge(19)), "(mss|severity)[^;]*7.*(emotion|e&b)"),
  "MisoQuest L2" = c(ge(61)), "S-Five L2" = c("87"), "SMS-Adult L2" = c("50\\.5|(>=|≥)\\s*51\\b"),
  "SMS-Adolescent L2" = c("49"),
  "DVMSQ L1" = c("subclinical"), "DVMSQ L2" = c("^(?!.*subclinical).*(clinical|algorithm)"),
  "DMQ L2" = c("1\\.8|41\\.4", paste0("impairment[^;]*", ge(14)), paste0("impairment[^;]*", ge(39))),
  "MAQ L1" = c(ge(12), ge(11)), "MAQ L2" = c(ge(25), ge(22), ge(24)),
  "MSL-CY L2" = c("(>=|≥)\\s*(10|9)\\b"), "DSTS-S L1" = c(ge(4)), "SSSQ4 L1" = c(ge(2)),
  "SSfM L1" = c("agree"), "SSfM L2" = c("."), "interview L3" = c("."))

# Rank of a threshold in Table 1 (1 = recommended); Inf if the threshold is not listed. For combined definitions
# (instrument 'multiple'), the best rank of any instrument named in the threshold.
table1_rank <- function(instrument, threshold, level) {
  t <- tolower(threshold)
  keys <- if (instrument == "multiple") {
    names(TABLE1)[endsWith(names(TABLE1), paste0(" ", level)) &
                    sapply(sub(" L[0-3]$", "", names(TABLE1)), function(i) grepl(tolower(i), t, fixed = TRUE))]
  } else paste(instrument, level)
  best <- Inf
  for (k in keys) {
    pats <- TABLE1[[k]]
    if (is.null(pats)) next
    hit <- which(vapply(pats, function(p) grepl(p, t, perl = TRUE), logical(1)))
    if (length(hit)) best <- min(best, hit[1])
  }
  best
}

# Choose one estimate among the rows of one sample at one level; returns the row and the rule that decided.
choose_one <- function(d) {
  if (nrow(d) == 1) return(list(row = d, rule = "only estimate"))
  why <- c()
  prim <- d |> filter(primary_for_authors == "yes")
  if (nrow(prim) > 0) {
    d <- d |> filter(instrument %in% prim$instrument)
    why <- c(why, "authors' primary instrument")
    if (nrow(d) == 1) return(list(row = d, rule = paste(why, collapse = "; ")))
  }
  if (all(d$level == "L1") && any(d$instrument != "adhoc")) {
    d <- d |> filter(instrument != "adhoc")   # rule G11: scale-based before self-identification and single items
    why <- c(why, "scale-based before ad hoc")
    if (nrow(d) == 1) return(list(row = d, rule = paste(why, collapse = "; ")))
  }
  rk <- mapply(table1_rank, d$instrument, d$threshold, d$level)
  keep <- if (SELECTION == "registered") rk == 1 else rk == min(rk)   # 'ordered': first listed threshold reported
  if (any(keep) && is.finite(min(rk))) {
    d <- d[keep, , drop = FALSE]
    why <- c(why, if (SELECTION == "registered") "Table 1 recommended threshold" else
      paste0("Table 1 threshold, rank ", min(rk)))
    if (nrow(d) == 1) return(list(row = d, rule = paste(why, collapse = "; ")))
  }
  lg <- qlogis(pmin(pmax(d$cases_n / d$n_n, 1e-6), 1 - 1e-6))
  o <- order(lg)
  pick <- o[ceiling(length(o) / 2)]   # median; with an even number, the lower of the two middle values
  list(row = d[pick, , drop = FALSE], rule = paste(c(why, "median logit"), collapse = "; "))
}

select_level <- function(data, levels, analysis) {
  out <- list(); log <- list()
  for (s in unique(data$sample_id)) {
    d <- data |> filter(sample_id == s, level %in% levels)
    if (nrow(d) == 0) next
    lv <- if ("L3" %in% d$level) "L3" else sort(unique(d$level), decreasing = TRUE)[1]   # L3 before L2
    d <- d |> filter(level == lv)
    ch <- choose_one(d)
    out[[s]] <- ch$row
    log[[s]] <- tibble(analysis = analysis, sample_id = s, estimate_id = ch$row$estimate_id, level = lv,
                       instrument = ch$row$instrument, threshold = ch$row$threshold,
                       cases = ch$row$cases_n, n = ch$row$n_n, candidates = nrow(d), rule = ch$rule)
  }
  list(data = bind_rows(out), log = bind_rows(log))
}

# ---------------------------------------------------------------------------------------------------------------
# Pooling
# ---------------------------------------------------------------------------------------------------------------

empty_row <- function(label, d, note) {
  tot <- function(col) if (nrow(d) == 0 || !col %in% names(d)) 0 else sum(d[[col]])
  tibble(analysis = label, k = nrow(d), n_total = tot("n_n"), cases_total = tot("cases_n"), prev = NA_real_,
         ci.lb = NA_real_, ci.ub = NA_real_, pi.lb = NA_real_, pi.ub = NA_real_, tau2 = NA_real_, I2 = NA_real_,
         method = NA_character_, note = note)
}

pool_glmm <- function(d, label) {
  if (nrow(d) < MIN_K) return(empty_row(label, d, sprintf("k < %d: not pooled", MIN_K)))
  m <- tryCatch(rma.glmm(measure = "PLO", xi = d$cases_n, ni = d$n_n, method = "ML"),
                error = function(e) e)
  if (inherits(m, "error")) return(empty_row(label, d, paste("GLMM failed:", conditionMessage(m))))
  p <- predict(m, transf = transf.ilogit)
  tibble(analysis = label, k = m$k, n_total = sum(d$n_n), cases_total = sum(d$cases_n), prev = p$pred,
         ci.lb = p$ci.lb, ci.ub = p$ci.ub, pi.lb = p$pi.lb, pi.ub = p$pi.ub, tau2 = m$tau2, I2 = m$I2,
         method = "GLMM (binomial-normal, ML)", note = "")
}

pool_iv <- function(d, label) {
  if (nrow(d) < MIN_K) return(empty_row(label, d, sprintf("k < %d: not pooled", MIN_K)))
  es <- escalc(measure = "PLO", xi = d$cases_n, ni = d$n_n)
  m <- rma(yi, vi, data = es, method = "REML", test = "knha")
  p <- predict(m, transf = transf.ilogit)
  tibble(analysis = label, k = m$k, n_total = sum(d$n_n), cases_total = sum(d$cases_n), prev = p$pred,
         ci.lb = p$ci.lb, ci.ub = p$ci.ub, pi.lb = p$pi.lb, pi.ub = p$pi.ub, tau2 = m$tau2, I2 = m$I2,
         method = "inverse variance, logit, REML + Hartung-Knapp", note = "")
}

subgroup_test <- function(d, var) {
  g <- d[[var]]
  keep <- !is.na(g)
  d <- d[keep, ]; g <- factor(g[keep])
  if (nlevels(g) < 2 || nrow(d) < MIN_K) return(tibble(moderator = var, QM = NA, df = NA, p = NA))
  m <- tryCatch(rma.glmm(measure = "PLO", xi = d$cases_n, ni = d$n_n, mods = ~ g, method = "ML"),
                error = function(e) NULL)
  if (is.null(m)) return(tibble(moderator = var, QM = NA, df = NA, p = NA))
  tibble(moderator = var, QM = m$QM, df = m$p - 1, p = m$QMp)
}

results <- list()
logs <- list()

# Primary outcome: L2/L3 in non-clinical samples (L3 if the sample has one, else L2).
nc <- whole |> filter(nonclinical)
sel_primary <- select_level(nc, c("L2", "L3"), "primary L2/L3")
prim <- sel_primary$data
logs$primary <- sel_primary$log
results$primary <- pool_glmm(prim, "Primary: L2/L3, non-clinical")

# Level-specific (section 13: the estimate at that level).
level_data <- list()
for (lv in c("L1", "L2", "L3")) {
  s <- select_level(nc, lv, paste("level", lv))
  level_data[[lv]] <- s$data
  logs[[paste0("level_", lv)]] <- s$log
  results[[paste0("level_", lv)]] <- pool_glmm(s$data, paste("Level", lv, "non-clinical"))
}

# Subgroups of the primary outcome (non-clinical samples).
for (v in c("poptype", "agegrp", "contgrp")) {
  for (g in sort(unique(prim[[v]]))) {
    results[[paste(v, g)]] <- pool_glmm(prim |> filter(.data[[v]] == g), paste0("Primary by ", v, ": ", g))
  }
}
sub_tests <- bind_rows(lapply(c("poptype", "agegrp", "contgrp"), function(v) subgroup_test(prim, v)))

# Clinical groups: whole-sample L2/L3 estimates of samples recruited for each diagnosis.
clin <- whole |> filter(!nonclinical)
sel_clin <- select_level(clin, c("L2", "L3"), "clinical L2/L3")
logs$clinical <- sel_clin$log
for (g in if (nrow(sel_clin$data) > 0) sort(unique(sel_clin$data$clin)) else character()) {
  results[[paste("clinical", g)]] <- pool_glmm(sel_clin$data |> filter(clin == g), paste("Clinical group:", g))
}

# ---------------------------------------------------------------------------------------------------------------
# Sensitivity analyses on the primary outcome (section 15c)
# ---------------------------------------------------------------------------------------------------------------

sens <- list()
sens$s1 <- pool_glmm(prim |> filter(prob), "S1 probability or census samples")
sens$s2 <- pool_glmm(prim |> filter(jbi_6 == "yes"), "S2 validated instrument and cut-off (JBI 6 = yes)")
sens$s3 <- pool_glmm(prim |> filter(jbi_9 %in% c("yes", "NA")), "S3 response rate >= 60% or not applicable (JBI 9)")
sens$s4 <- pool_glmm(prim |> filter(topic_disclosed != "yes"), "S4 topic not disclosed at recruitment")
sens$s5 <- pool_glmm(prim |> filter(journal), "S5 journal articles only")
sens$s6 <- pool_glmm(prim |> filter(n_n >= 100), "S6 n >= 100")
sens$s7 <- pool_iv(prim, "S7 inverse-variance pooling of logits (REML, Hartung-Knapp)")
hi <- nc |> filter(level %in% c("L2", "L3")) |> group_by(sample_id) |> slice_min(cases_n / n_n, n = 1, with_ties = FALSE) |> ungroup()
lo <- nc |> filter(level %in% c("L2", "L3")) |> group_by(sample_id) |> slice_max(cases_n / n_n, n = 1, with_ties = FALSE) |> ungroup()
sens$s8a <- pool_glmm(hi, "S8 highest threshold per sample (lowest prevalence)")
sens$s8b <- pool_glmm(lo, "S8 lowest threshold per sample (highest prevalence)")
sens$s10 <- pool_glmm(prim |> filter(level == "L2"), "S10 L2 only (L3 excluded)")
# Post hoc (deviations.md, 2026-10-15): when the recommended threshold is not reported, the next threshold listed in
# Table 1 (e.g., AMISOS-R >= 21, MAQ >= 22) instead of the median of the remaining estimates.
SELECTION <- "ordered"
sel_ordered <- select_level(nc, c("L2", "L3"), "post hoc: ordered Table 1 thresholds")
SELECTION <- "registered"
logs$ordered <- sel_ordered$log
sens$s11 <- pool_glmm(sel_ordered$data, "S11 (post hoc) next Table 1 threshold before the median rule")
for (g in sort(unique(sel_ordered$data$poptype))) {
  sens[[paste("s11", g)]] <- pool_glmm(sel_ordered$data |> filter(poptype == g), paste("S11 (post hoc) by poptype:", g))
}

# S9: leave-one-out (GLMM) and influence diagnostics (inverse-variance model).
loo <- NULL; infl <- NULL
if (nrow(prim) > MIN_K) {
  loo <- bind_rows(lapply(seq_len(nrow(prim)), function(i) {
    r <- pool_glmm(prim[-i, ], paste("without", prim$sample_id[i]))
    r$sample_id <- prim$sample_id[i]
    r
  }))
  es <- escalc(measure = "PLO", xi = prim$cases_n, ni = prim$n_n)
  m <- rma(yi, vi, data = es, method = "REML", test = "knha")
  inf <- influence(m)
  infl <- tibble(sample_id = prim$sample_id, rstudent = inf$inf$rstudent, cook = inf$inf$cook.d,
                 influential = inf$is.infl)
}

# ---------------------------------------------------------------------------------------------------------------
# Three-level moderator analysis on all whole-sample estimates of non-clinical samples (section 15b)
# ---------------------------------------------------------------------------------------------------------------

zs <- function(x) as.numeric(scale(x))   # continuous moderators centred and scaled, so that glmer converges
ml <- nc |> mutate(est_id = row_number(), level = factor(level), poptype = factor(poptype),
                   age_z = zs(age_mean_n), female_z = zs(pct_female_n), year_z = zs(year_data))
re_terms <- function(g) paste0("(1 | ", names(getME(g, "flist")), ")")   # random intercepts a fitted model kept
fit_glmer <- function(formula_fixed, data, re = c("(1 | study_id)", "(1 | sample_id)", "(1 | est_id)"),
                      drop = TRUE) {
  repeat {
    f <- as.formula(paste("cbind(cases_n, n_n - cases_n) ~", formula_fixed, "+", paste(re, collapse = " + ")))
    g <- tryCatch(glmer(f, data = data, family = binomial,
                        control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 2e5))),
                  error = function(e) NULL)
    if (is.null(g)) return(NULL)
    if (!drop || !isSingular(g) || length(re) == 1) return(g)
    vc <- as.data.frame(VarCorr(g))
    zero <- vc$grp[which.min(vc$vcov)]
    re <- re[!grepl(paste0("\\| ", zero, "\\)"), re)]   # drop the variance component estimated at zero
  }
}
multilevel <- list()
if (nrow(ml) >= MIN_K_MOD) {
  multilevel$prespecified <- fit_glmer("level + poptype + prob", ml)
  es_ml <- escalc(measure = "PLO", xi = ml$cases_n, ni = ml$n_n, data = ml)
  mv <- tryCatch(rma.mv(yi, vi, mods = ~ level + poptype + prob, random = ~ 1 | study_id / sample_id / est_id,
                        data = es_ml, method = "REML"), error = function(e) NULL)
  multilevel$rma_mv <- mv
  multilevel$robust <- if (!is.null(mv)) coef_test(mv, vcov = "CR2", cluster = es_ml$study_id) else NULL
  explore <- c("age_z", "female_z", "contgrp", "who_region", "income_group", "mode", "topic_disclosed",
               "jbi_2", "jbi_6", "jbi_9", "journal", "year_z")
  # One moderator at a time, adjusted for level; likelihood-ratio test against the model without it, with the same
  # random part. 'instrument' is tested within L2 (no level term). Coefficients (odds ratios) go to a second table.
  coefs <- list()
  lrt <- function(v, d, base) {
    k <- length(unique(d$sample_id))
    if (k < MIN_K_MOD || length(unique(d[[v]])) < 2) {
      return(tibble(moderator = v, k_samples = k, chisq = NA, df = NA, p = NA,
                    note = "k < 10 or no variation: not tested"))
    }
    g1 <- fit_glmer(paste(base, "+", v), d)
    g0 <- if (is.null(g1)) NULL else fit_glmer(base, d, re = re_terms(g1), drop = FALSE)   # same random part
    if (is.null(g1) || is.null(g0)) return(tibble(moderator = v, k_samples = k, chisq = NA, df = NA, p = NA,
                                                   note = "model failed"))
    a <- anova(g0, g1)
    cf <- summary(g1)$coefficients
    cf <- cf[startsWith(rownames(cf), v), , drop = FALSE]
    ref <- if (is.numeric(d[[v]])) "per SD" else levels(factor(d[[v]]))[1]
    coefs[[v]] <<- tibble(moderator = v, term = rownames(cf), reference = ref, OR = exp(cf[, 1]),
                          ci.lb = exp(cf[, 1] - 1.96 * cf[, 2]), ci.ub = exp(cf[, 1] + 1.96 * cf[, 2]),
                          p = cf[, 4], n_estimates = nrow(d),
                          n_samples_term = vapply(rownames(cf), function(t) {
                            lv <- substring(t, nchar(v) + 1)
                            if (is.numeric(d[[v]])) k else length(unique(d$sample_id[d[[v]] == lv]))
                          }, integer(1)))
    tibble(moderator = v, k_samples = k, chisq = a$Chisq[2], df = a$Df[2], p = a$`Pr(>Chisq)`[2],
           note = if (base == "level") "likelihood-ratio test, adjusted for level" else
             "likelihood-ratio test, L2 estimates only")
  }
  multilevel$exploratory <- bind_rows(
    lapply(explore, function(v) lrt(v, ml |> filter(!is.na(.data[[v]]), .data[[v]] != "", .data[[v]] != "NR"),
                                    "level")),
    lrt("instrument", ml |> filter(level == "L2"), "1"))
  multilevel$exploratory_coefs <- bind_rows(coefs)
  # Share of the between-estimate variance (all three levels, logit scale) explained by the case-definition level,
  # by level + instrument, and by the pre-specified model: pseudo-R2 = 1 - total variance / total variance of the null.
  vtot <- function(m) if (is.null(m)) NA_real_ else sum(as.data.frame(VarCorr(m))$vcov)
  g_null <- fit_glmer("1", ml)
  r2 <- function(m) 1 - vtot(m) / vtot(g_null)
  multilevel$variance_explained <- tibble(
    model = c("level", "level + instrument", "level + population type + probability sampling"),
    total_variance = c(vtot(fit_glmer("level", ml)), vtot(fit_glmer("level + instrument", ml)),
                       vtot(multilevel$prespecified)),
    null_variance = vtot(g_null)) |>
    mutate(pseudo_R2 = 1 - total_variance / null_variance)
  # Instrument within L2
  l2 <- ml |> filter(level == "L2")
  if (length(unique(l2$sample_id)) >= MIN_K_MOD && length(unique(l2$instrument)) > 1) {
    multilevel$instrument_L2 <- fit_glmer("instrument", l2)
  }
}

# ---------------------------------------------------------------------------------------------------------------
# Sex difference (log odds ratio, female vs male, at the sample's L2/L3 definition)
# ---------------------------------------------------------------------------------------------------------------

sexdat <- ests |> filter(nonclinical, level %in% c("L2", "L3"), sub %in% c("female", "male"),
                         !is.na(cases_n), !is.na(n_n), n_n > 0)
sex_rows <- list()
for (s in unique(sexdat$sample_id)) {
  d <- sexdat |> filter(sample_id == s)
  p <- prim |> filter(sample_id == s)
  pairs <- d |> group_by(instrument, level) |> filter(all(c("female", "male") %in% sub)) |> ungroup()
  if (nrow(pairs) == 0) next
  if (nrow(p) == 1 && any(pairs$instrument == p$instrument & pairs$level == p$level)) {
    pairs <- pairs |> filter(instrument == p$instrument, level == p$level)
  }
  f <- pairs |> filter(sub == "female") |> slice(1)
  m <- pairs |> filter(sub == "male") |> slice(1)
  sex_rows[[s]] <- tibble(sample_id = s, instrument = f$instrument, level = f$level,
                          f_cases = f$cases_n, f_n = f$n_n, m_cases = m$cases_n, m_n = m$n_n)
}
sex <- bind_rows(sex_rows)
sex_result <- NULL
if (nrow(sex) >= MIN_K) {
  es <- escalc(measure = "OR", ai = sex$f_cases, n1i = sex$f_n, ci = sex$m_cases, n2i = sex$m_n)
  sm <- rma(yi, vi, data = es, method = "REML", test = "knha")
  sp <- predict(sm, transf = exp)
  sex_result <- tibble(k = sm$k, OR = sp$pred, ci.lb = sp$ci.lb, ci.ub = sp$ci.ub, pi.lb = sp$pi.lb,
                       pi.ub = sp$pi.ub, tau2 = sm$tau2, I2 = sm$I2)
}

# ---------------------------------------------------------------------------------------------------------------
# Meta-biases (section 16) and GRADE inputs (section 17)
# ---------------------------------------------------------------------------------------------------------------

bias <- NULL; grade <- NULL
if (nrow(prim) >= MIN_K) {
  es <- escalc(measure = "PLO", xi = prim$cases_n, ni = prim$n_n, data = prim)
  es$inv_sqrt_n <- 1 / sqrt(es$n_n)
  reg <- rma(yi, vi, mods = ~ inv_sqrt_n, data = es, method = "REML", test = "knha")
  pubm <- tryCatch(rma.glmm(measure = "PLO", xi = prim$cases_n, ni = prim$n_n, mods = ~ prim$journal,
                            method = "ML"), error = function(e) NULL)
  bias <- tibble(test = c("logit prevalence on 1/sqrt(n) (REML, Hartung-Knapp)", "journal vs other (GLMM)"),
                 estimate = c(coef(reg)[2], if (is.null(pubm)) NA else coef(pubm)[2]),
                 p = c(reg$pval[2], if (is.null(pubm)) NA else pubm$pval[2]))
  ggplot(es, aes(x = yi, y = sqrt(vi))) + geom_point() + scale_y_reverse() +
    labs(x = "Logit prevalence", y = "Standard error", title = "Primary outcome: logit prevalence vs standard error") +
    theme_minimal()
  ggsave(file.path(fig_dir, "bias_logit_vs_se.png"), width = 6, height = 4.5, dpi = 300)
}

# GRADE inputs for the summary-of-findings rows: share of the inverse-variance weight from samples rated 'no' on JBI
# items 2, 6 and 9 (risk of bias), interval widths (inconsistency, imprecision), countries and continents
# (indirectness) and the small-study regression when k >= 10 (publication bias).
grade_one <- function(d, label, r, yi, vi, measure) {
  m <- rma(yi, vi, method = "REML")
  w <- weights(m) / 100
  j <- samples[match(d$sample_id, samples$sample_id), ]
  no <- function(x) !is.na(x) & x == "no"
  reg <- if (measure == "prevalence" && nrow(d) >= 10) {
    tryCatch(rma(yi, vi, mods = ~ I(1 / sqrt(d$n_n)), method = "REML", test = "knha"), error = function(e) NULL)
  } else NULL
  ctry <- j$country[!grepl("^MULTI", toupper(j$country)) & !j$country %in% c("NR", "")]
  tibble(outcome = label, measure = measure, k = nrow(d),
         participants = if (measure == "prevalence") sum(d$n_n) else sum(d$f_n + d$m_n),
         estimate = if (measure == "prevalence") r$prev else r$OR, ci.lb = r$ci.lb, ci.ub = r$ci.ub,
         pi.lb = r$pi.lb, pi.ub = r$pi.ub,
         weight_jbi2_no = sum(w[no(j$jbi_2)]), weight_jbi6_no = sum(w[no(j$jbi_6)]), weight_jbi9_no = sum(w[no(j$jbi_9)]),
         weight_any_no = sum(w[no(j$jbi_2) | no(j$jbi_6) | no(j$jbi_9)]),
         countries = length(unique(ctry)), continents = length(unique(na.omit(j$contgrp))),
         small_study_p = if (is.null(reg)) NA_real_ else reg$pval[2])
}
grade_rows <- list()
plo <- function(d) escalc(measure = "PLO", xi = d$cases_n, ni = d$n_n)
if (nrow(prim) >= MIN_K) {
  e <- plo(prim)
  grade_rows$primary <- grade_one(prim, "Clinically significant (L2/L3), non-clinical samples", results$primary,
                                  e$yi, e$vi, "prevalence")
  pg <- prim |> filter(poptype == "probability general population")
  if (nrow(pg) >= MIN_K) {
    e <- plo(pg)
    grade_rows$prob <- grade_one(pg, "Clinically significant (L2/L3), probability samples of the general population",
                                 results[["poptype probability general population"]], e$yi, e$vi, "prevalence")
  }
}
if (!is.null(level_data$L1) && nrow(level_data$L1) >= MIN_K) {
  e <- plo(level_data$L1)
  grade_rows$l1 <- grade_one(level_data$L1, "Symptom level (L1), non-clinical samples", results$level_L1,
                             e$yi, e$vi, "prevalence")
}
if (!is.null(sex_result)) {
  e <- escalc(measure = "OR", ai = sex$f_cases, n1i = sex$f_n, ci = sex$m_cases, n2i = sex$m_n)
  grade_rows$sex <- grade_one(sex, "Female-to-male odds ratio, clinically significant (L2/L3)", sex_result,
                              e$yi, e$vi, "odds ratio")
}
grade <- if (length(grade_rows)) bind_rows(grade_rows[intersect(c("primary", "l1", "prob", "sex"), names(grade_rows))]) else NULL

# ---------------------------------------------------------------------------------------------------------------
# Figures and tables
# ---------------------------------------------------------------------------------------------------------------

if (nrow(prim) > 0) {
  cp <- function(x, n) {   # Clopper-Pearson
    lo <- ifelse(x == 0, 0, qbeta(0.025, x, n - x + 1))
    hi <- ifelse(x == n, 1, qbeta(0.975, x + 1, n - x))
    cbind(lo, hi)
  }
  ci <- cp(prim$cases_n, prim$n_n)
  # Row labels: first author, year (a, b... for several samples of one report), instrument and level.
  inst_lab <- function(i) case_when(i == "multiple" ~ "combined", i == "adhoc" ~ "ad hoc items", TRUE ~ i)
  pop_order <- c("probability general population", "other general population", "university students",
                 "school children and adolescents", "other non-clinical")
  fd <- prim |>
    mutate(p = cases_n / n_n, lo = ci[, 1], hi = ci[, 2],
           author = ifelse(first_author == toupper(first_author), tools::toTitleCase(tolower(first_author)),
                           first_author),
           ay = paste(author, year)) |>
    group_by(ay) |> mutate(ay = if (n() > 1) paste0(ay, letters[seq_len(n())]) else ay) |> ungroup() |>
    mutate(lab = paste0(ay, " (", inst_lab(instrument), ", ", level, ")"), pooled = FALSE)
  pooled_rows <- bind_rows(lapply(split(fd, fd$poptype), function(d) {
    r <- pool_glmm(d, "")
    tibble(poptype = d$poptype[1], p = r$prev, lo = r$ci.lb, hi = r$ci.ub,
           lab = sprintf("Pooled, k = %d", r$k), pooled = TRUE)
  })) |> filter(!is.na(p))
  fd <- bind_rows(fd, pooled_rows) |>
    mutate(poptype = factor(poptype, levels = pop_order,
                            labels = paste0(toupper(substr(pop_order, 1, 1)), substring(pop_order, 2))),
           id = paste(poptype, lab)) |>
    arrange(poptype, desc(pooled), desc(p))
  fd$id <- factor(fd$id, levels = unique(fd$id))   # first level at the bottom: pooled row last, lowest value on top
  ggplot(fd, aes(x = p, y = id)) +
    geom_errorbar(aes(xmin = lo, xmax = hi), width = 0.25, orientation = "y", linewidth = 0.3) +
    geom_point(aes(shape = pooled, size = pooled)) +
    scale_shape_manual(values = c(`FALSE` = 16, `TRUE` = 18), guide = "none") +
    scale_size_manual(values = c(`FALSE` = 1.2, `TRUE` = 3), guide = "none") +
    scale_y_discrete(labels = setNames(fd$lab, fd$id)) +
    facet_grid(poptype ~ ., scales = "free_y", space = "free_y", labeller = label_wrap_gen(width = 16)) +
    geom_vline(xintercept = results$primary$prev, linetype = "dashed", linewidth = 0.3) +
    scale_x_continuous(labels = scales::percent, breaks = seq(0, 1, 0.1)) +
    labs(x = "Prevalence (95% CI)", y = NULL) +
    theme_minimal(base_size = 7.5) +
    theme(strip.text.y = element_text(angle = 0, hjust = 0), panel.grid.minor = element_blank(),
          panel.spacing = unit(0.6, "lines"))
  ggsave(file.path(fig_dir, "forest_primary.png"), width = 7, height = max(4, 0.15 * nrow(fd) + 1.2), dpi = 300,
         bg = "white")
  ggsave(file.path(fig_dir, "forest_primary.pdf"), width = 7, height = max(4, 0.15 * nrow(fd) + 1.2))
}
emap <- ests |> filter(sub %in% c("all", "total", "whole sample")) |> count(instrument, level)
if (nrow(emap) > 0) {
  ggplot(emap, aes(x = level, y = instrument, fill = n)) + geom_tile() + geom_text(aes(label = n), size = 3) +
    scale_fill_gradient(low = "grey90", high = "grey40") +
    labs(x = "Case-definition level", y = NULL, title = "Evidence map: whole-sample estimates") + theme_minimal()
  ggsave(file.path(fig_dir, "evidence_map.png"), width = 6, height = 4.5, dpi = 300)
}

listed <- ests |> filter(!level %in% c("L1", "L2", "L3") | !poolable) |>
  select(estimate_id, sample_id, subgroup, instrument, threshold, level, cases, n, notes)

# ---------------------------------------------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------------------------------------------

pooled <- bind_rows(results)
write_csv(pooled, file.path(res_dir, "pooled.csv"))
write_csv(bind_rows(sens), file.path(res_dir, "sensitivity.csv"))
write_csv(bind_rows(logs), file.path(res_dir, "selection_log.csv"))
write_csv(sub_tests, file.path(res_dir, "subgroup_tests.csv"))
write_csv(listed, file.path(res_dir, "listed_not_pooled.csv"))
if (!is.null(loo)) write_csv(loo, file.path(res_dir, "leave_one_out.csv"))
if (!is.null(infl)) write_csv(infl, file.path(res_dir, "influence.csv"))
if (nrow(sex) > 0) write_csv(sex, file.path(res_dir, "sex_data.csv"))
if (!is.null(sex_result)) write_csv(sex_result, file.path(res_dir, "sex_or.csv"))
if (!is.null(bias)) write_csv(bias, file.path(res_dir, "meta_bias.csv"))
if (!is.null(grade)) write_csv(grade, file.path(res_dir, "grade_inputs.csv"))
if (!is.null(multilevel$prespecified)) {
  cf <- summary(multilevel$prespecified)$coefficients
  write_csv(tibble(term = rownames(cf), log_or = cf[, 1], se = cf[, 2], OR = exp(cf[, 1]),
                   ci.lb = exp(cf[, 1] - 1.96 * cf[, 2]), ci.ub = exp(cf[, 1] + 1.96 * cf[, 2]), p = cf[, 4]),
            file.path(res_dir, "multilevel_prespecified.csv"))
}
if (!is.null(multilevel$robust)) write_csv(as_tibble(multilevel$robust), file.path(res_dir, "multilevel_robust.csv"))
if (!is.null(multilevel$variance_explained)) write_csv(multilevel$variance_explained,
                                                         file.path(res_dir, "variance_explained.csv"))
if (!is.null(multilevel$exploratory)) write_csv(multilevel$exploratory, file.path(res_dir, "moderators_exploratory.csv"))
if (!is.null(multilevel$exploratory_coefs)) write_csv(multilevel$exploratory_coefs,
                                                        file.path(res_dir, "moderators_exploratory_coefs.csv"))
sink(file.path(res_dir, "multilevel.txt"))
for (nm in names(multilevel)) {
  cat("\n=====", nm, "=====\n")
  print(if (inherits(multilevel[[nm]], "merMod")) summary(multilevel[[nm]]) else multilevel[[nm]])
}
sink()
writeLines(capture.output(sessionInfo()), file.path(out_root, "sessionInfo.txt"))

fmt <- function(x) ifelse(is.na(x), "NA", sprintf("%.1f%%", 100 * x))
cat("Primary (L2/L3, non-clinical): k =", results$primary$k, " prevalence", fmt(results$primary$prev),
    "(95% CI", fmt(results$primary$ci.lb), "-", fmt(results$primary$ci.ub), "; PI", fmt(results$primary$pi.lb),
    "-", fmt(results$primary$pi.ub), ")\n")
cat("Results in", res_dir, "\n")
