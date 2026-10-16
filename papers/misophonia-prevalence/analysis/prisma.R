# PRISMA 2020 flow diagram (identification of new studies via databases, registers and other sources).
#
# Reads fulltext/prisma_counts.json (search -> screening -> full texts) and, when the verified tables exist,
# forms/samples.csv (studies and samples in the review); writes analysis/figures/prisma.png and prisma.pdf.
# Run from the repository root: Rscript papers/misophonia-prevalence/analysis/prisma.R

suppressPackageStartupMessages({
  library(ggplot2)
  library(jsonlite)
})

paper <- "papers/misophonia-prevalence"
pc <- fromJSON(file.path(paper, "fulltext", "prisma_counts.json"))
fig_dir <- file.path(paper, "analysis", "figures")
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)
fmt <- function(x) prettyNum(x, big.mark = ",")

src_names <- c(pubmed = "PubMed", europepmc = "Europe PMC", openalex = "OpenAlex", s2 = "Semantic Scholar",
               citations = "Citations of instrument papers (OpenAlex)", scielo = "SciELO", datacite = "DataCite",
               openaire = "OpenAIRE", core = "CORE", scholar = "Google Scholar")
by_src <- pc$by_source
src_txt <- paste(sprintf("%s (n = %s)", src_names[names(by_src)], fmt(unlist(by_src))), collapse = "\n")
excl <- pc$reports_excluded
excl_names <- c(E1_selected_sample = "Recruited for misophonia or sound sensitivity",
                I3_no_counts = "No number of cases with a denominator",
                E4_design = "Design (review, case report, qualitative)",
                other = "Other", E2_no_misophonia_measure = "No misophonia-specific measure",
                not_misophonia = "Not about misophonia")
excl_txt <- paste(sprintf("%s (n = %s)", excl_names[names(excl)], fmt(unlist(excl))), collapse = "\n")

studies_txt <- "Studies included in review (n = 95)\nReports of included studies (n = 119)"
sp <- file.path(paper, "forms", "samples.csv")
if (file.exists(sp) && length(readLines(sp)) > 1) {
  s <- read.csv(sp, colClasses = "character")
  studies_txt <- sprintf("Studies included in review (n = %d)\nIndependent samples (n = %d)\nReports of included studies (n = %d)",
                         length(unique(s$study_id)), nrow(s), pc$reports_included)
}

boxes <- data.frame(
  x = c(1, 3, 1, 3, 1, 3, 1, 3, 1),
  y = c(9, 9, 7, 7, 5, 5, 3, 3, 1),
  w = c(1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8),
  h = c(1.9, 1.4, 0.8, 0.8, 0.8, 0.8, 0.8, 1.6, 1.0),
  label = c(
    paste0("Records identified (n = ", fmt(pc$records_identified), "):\n", src_txt),
    paste0("Records removed before screening:\nDuplicate records (n = ", fmt(pc$duplicates_removed),
           ")\nRemoved by automation tools\n(non-study records, n = ", fmt(pc$removed_by_automation), ")"),
    paste0("Records screened\n(n = ", fmt(pc$records_screened), ")"),
    paste0("Records excluded\n(n = ", fmt(pc$records_excluded), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(pc$reports_sought), ")"),
    paste0("Reports not retrieved\n(no open-access full text; n = ", fmt(pc$reports_not_retrieved), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(pc$reports_assessed), ")"),
    paste0("Reports excluded (n = ", fmt(sum(unlist(excl))), "):\n", excl_txt),
    studies_txt),
  stringsAsFactors = FALSE)
arrows <- data.frame(
  x = c(1, 1.9, 1, 1.9, 1, 1.9, 1, 1.9), y = c(9 - 0.95, 9, 7 - 0.4, 7, 5 - 0.4, 5, 3 - 0.4, 3),
  xend = c(1, 2.1, 1, 2.1, 1, 2.1, 1, 2.1), yend = c(7 + 0.4, 9, 5 + 0.4, 7, 3 + 0.4, 5, 1 + 0.5, 3))
xmax <- 4
labels_y <- c(9, 6, 1)

# Identification via other methods: citation searching of the included studies (search/citation_chase.py).
cl <- file.path(paper, "search", "runs", "2026-10-15-citations", "chase_log.json")
if (file.exists(cl)) {
  ch <- fromJSON(cl)
  rl <- read.csv(file.path(paper, "fulltext", "retrieval_log.csv"), colClasses = "character", check.names = FALSE)
  names(rl)[1] <- "rec_id"
  rl <- rl[grepl("^R2[0-9]{3}$", rl$rec_id), ]
  sought <- nrow(rl)
  got <- sum(rl$status == "retrieved")
  dec_txt <- "Reports excluded:\n(decisions pending)"
  inc_n <- NA
  dp <- file.path(paper, "fulltext", "decisions", "ft_R1_chase.csv")
  if (file.exists(dp)) {
    d <- read.csv(dp, colClasses = "character", check.names = FALSE)
    names(d)[1] <- "rec_id"
    ex <- table(d$reason[d$decision == "not_eligible"])
    dec_txt <- paste0("Reports excluded (n = ", sum(ex), "):\n",
                      paste(sprintf("%s (n = %s)", excl_names[names(ex)], fmt(as.integer(ex))), collapse = "\n"))
    inc_n <- sum(d$decision == "eligible")
  }
  other <- data.frame(
    x = c(5, 7, 5, 7, 5, 7), y = c(9, 7, 5, 5, 3, 3), w = 1.8, h = c(1.2, 1.2, 0.8, 0.8, 0.8, 1.6),
    label = c(
      paste0("Records identified from citation\nsearching of included studies\n(not in the database set; n = ",
             fmt(ch$new_unique_records), ")"),
      paste0("Records not sought: no condition term\nin title, abstract or OpenAlex\nfull text (n = ",
             fmt(ch$new_unique_records - ch$fulltext_search$records_matching), ")"),
      paste0("Reports sought for retrieval\n(n = ", fmt(sought), ")"),
      paste0("Reports not retrieved\n(no open-access full text; n = ", fmt(sought - got), ")"),
      paste0("Reports assessed for eligibility\n(n = ", fmt(got), ")"),
      dec_txt),
    stringsAsFactors = FALSE)
  boxes <- rbind(boxes, other)
  arrows <- rbind(arrows, data.frame(
    x = c(5, 5, 5.9, 5, 5.9, 5), y = c(9 - 0.6, 7, 5, 5 - 0.4, 3, 3 - 0.4),
    xend = c(5, 6.1, 6.1, 5, 6.1, 1.9), yend = c(5 + 0.4, 7, 5, 3 + 0.4, 3, 1)))
  arrows <- arrows[-c(nrow(arrows) - 4), ]   # the line to 'not sought' starts from the identification box
  arrows <- rbind(arrows, data.frame(x = 5, y = 7, xend = 6.1, yend = 7))
  if (!is.na(inc_n) && exists("s")) {
    boxes$label[9] <- sprintf(paste0("Studies included in review (n = %d)\nIndependent samples (n = %d)\n",
                                     "Reports of included studies (n = %d)\n(from citation searching: %d)"),
                              length(unique(s$study_id)), nrow(s), pc$reports_included + inc_n, inc_n)
  }
  xmax <- 8
}

p <- ggplot() +
  geom_rect(data = boxes, aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2),
            fill = "white", colour = "black", linewidth = 0.3) +
  geom_text(data = boxes, aes(x = x, y = y, label = label), size = 2.3, lineheight = 0.95) +
  geom_segment(data = arrows, aes(x = x, y = y, xend = xend, yend = yend),
               arrow = arrow(length = unit(0.12, "cm"), type = "closed"), linewidth = 0.3) +
  annotate("text", x = -0.25, y = labels_y, label = c("Identification", "Screening", "Included"),
           angle = 90, size = 2.8, fontface = "bold") +
  annotate("text", x = c(2, 6)[seq_len(if (xmax > 4) 2 else 1)], y = 10.35,
           label = c("Databases, search engines and instrument citations", "Citation searching of included studies")[seq_len(if (xmax > 4) 2 else 1)],
           size = 2.8, fontface = "bold") +
  coord_cartesian(xlim = c(-0.4, xmax), ylim = c(0.3, 10.5)) +
  theme_void()
ggsave(file.path(fig_dir, "prisma.png"), p, width = if (xmax > 4) 12 else 7, height = 8.3, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "prisma.pdf"), p, width = if (xmax > 4) 12 else 7, height = 8.3)
cat("PRISMA flow diagram ->", fig_dir, "\n")
