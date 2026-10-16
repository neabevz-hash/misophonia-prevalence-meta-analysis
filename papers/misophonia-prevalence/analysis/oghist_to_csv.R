# World Bank income groups by fiscal year, from the World Bank's historical classification file (OGHIST.xlsx,
# sheet "Country Analytical History"; downloaded 2026-10-15 from
# https://datacatalogfiles.worldbank.org/ddh-published/0037712/DR0090754/OGHIST.xlsx, the World Bank Data Catalog copy, which
# runs to FY25; stored as analysis/data/OGHIST_2026-10-15.xlsx).
# Writes analysis/data/wb_income_history.csv: iso3, fiscal_year (e.g. 2021 = FY21, July 2020 - June 2021),
# gni_year (the calendar year whose GNI per capita set the group), group (low / lower-middle / upper-middle / high).
# Run from the repository root: Rscript papers/misophonia-prevalence/analysis/oghist_to_csv.R

suppressMessages(library(readxl))
dir <- "papers/misophonia-prevalence/analysis/data"
x <- suppressMessages(read_excel(file.path(dir, "OGHIST_2026-10-15.xlsx"), sheet = "Country Analytical History",
                                 col_names = FALSE))
fy <- unlist(x[5, ])        # "FY89" ...
gni <- unlist(x[6, ])       # 1987 ...
cols <- which(grepl("^FY[0-9]{2}$", fy))
rows <- which(grepl("^[A-Z]{3}$", x[[1]]))
code <- c(L = "low", LM = "lower-middle", UM = "upper-middle", H = "high")
out <- do.call(rbind, lapply(rows, function(r) {
  v <- trimws(unlist(x[r, cols]))
  y2 <- as.integer(sub("FY", "", fy[cols]))
  data.frame(iso3 = x[[1]][r], fiscal_year = ifelse(y2 >= 80, 1900 + y2, 2000 + y2),
             gni_year = as.integer(gni[cols]), group = unname(code[v]), stringsAsFactors = FALSE)
}))
out <- out[!is.na(out$group), ]
write.csv(out, file.path(dir, "wb_income_history.csv"), row.names = FALSE, fileEncoding = "UTF-8")
cat(nrow(out), "country-years,", length(unique(out$iso3)), "countries, fiscal years", min(out$fiscal_year), "-",
    max(out$fiscal_year), "\n")
