install.packages("enrichR")

data <- read.csv("final_approved_by_sir.csv", header = TRUE)
all <- read.csv("final_approved_by_sir.csv", header = TRUE)

up.idx <- which(data$pval < 0.05 & data$logFC > 1.5)
dn.idx <- which(data$pval < 0.05 & data$logFC < -1.5)

all.genes <- data$geneNames
up.genes <- data[up.idx,]$geneNames
dn.genes <- data[dn.idx,]$geneNames
#For KEGG Pathway Analysis
DisGeNET
Cancer_Cell_Line_Encyclopedia
ClinVar_2019
GO_Biological_Process_2021
GO_Cellular_Component_2021
GO_Molecular_Function_2021
Human_Phenotype_Ontology
KEGG_2019_Human
OMIM_Disease
Panther_2016
Reactome_2016
WikiPathways_2019_Human

library(enrichR)
dbs_pw <- c("KEGG_2019_Human")

upEnriched_pw <- enrichr(genes = up.genes, databases = dbs_pw)
dnEnriched_pw <- enrichr(genes = dn.genes, databases = dbs_pw)


plotEnrich(upEnriched_pw[[1]], showTerms = 15, numChar = 40, y = "Ratio", orderBy = "P.value", title = "KEGG Pathways - Upregulated Genes")


plotEnrich(dnEnriched_pw[[1]], showTerms = 15, numChar = 40, y = "Ratio", orderBy = "P.value", title = "KEGG Pathways - Downregulated Genes")

write.csv(upEnriched_pw[1], "up_reactome.csv")
write.csv(dnEnriched_pw[1], "dn_reactome.csv")