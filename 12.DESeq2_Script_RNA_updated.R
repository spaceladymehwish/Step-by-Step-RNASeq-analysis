#BiocManager::install("DESeq2")

#Import DESeq2 library in R
library("DESeq2")
library(dplyr)
install.packages("tidyr")
library(tidyr)
library(EnhancedVolcano)
#Load gene(/transcript) count matrix and labels
countData <- as.matrix(read.csv("gene_count_matrix.csv", row.names="gene_id"))
colData <- read.csv("metadata_file.csv", sep=",", row.names = 1)

#Note: The PHENO_DATA file contains information on each sample, e.g., sex or population. The exact way to import this depends on the format of the file.
#Check all sample IDs in colData are also in CountData and match their orders

rownames(colData)

all(rownames(colData) %in% colnames(countData))

countData <- countData[, rownames(colData)]

all(rownames(colData) == colnames(countData))

#Create a DESeqDataSet from count matrix and labels
dds <- DESeqDataSetFromMatrix(countData = countData,
                              colData = colData, design = ~ type)
#Run the default analysis for DESeq2 and generate results table

dds <- DESeq(dds)

res <- results(dds)


#Sort by adjusted p-value and display
(resOrdered <- res[order(res$padj), ])

head(results(dds, tidy=TRUE))
summary(res)

res <- res[order(res$pvalue), ]
head(res)

write.csv(as.data.frame(res), file="deseq2_degs_melanoma.csv")



degs <- read.csv("deseq2_degs_melanoma.csv")
names <- data.frame(do.call('rbind', strsplit(as.character(degs$X),'|',fixed=TRUE)))
degs <- cbind(degs, names)
degs$X2 <- sub("^MSTRG.*", ".", degs$X2)
final_without_dots <- subset(degs, X2!=".")

final_set <- subset(final_without_dots, log2FoldChange < -1 & pvalue < 0.05 | log2FoldChange > 1 & pvalue < 0.05)
downreg <- subset(final_without_dots, log2FoldChange < -1 & pvalue < 0.05)
upreg <- subset(final_without_dots, log2FoldChange > 1 & pvalue < 0.05)


# sorting of down and up regulated genes
sorted_downreg <- (arrange(downreg,log2FoldChange))
sorted_upreg <- upreg %>% arrange(desc(log2FoldChange))

write.csv(sorted_downreg,"sorted_downregulated_melanoma.csv")
write.csv(sorted_upreg,"sorted_upregulated_melanoma.csv")

# To retrieve top 10 dysregulated genes
top10_downreg <- head(arrange(downreg,log2FoldChange), 10)
top10_upreg <- upreg %>% arrange(desc(log2FoldChange)) %>% head(10)


write.csv(top10_downreg,"top10_downregulated_melanoma.csv")
write.csv(top10_upreg,"top10_upregulated_melanoma.csv")



write.csv(downreg,"final_downregulated_melanoma.csv")
write.csv(upreg,"final_upregulated_melanoma.csv")
write.csv(final_set,"final_upregulated_and_downregulated_melanoma.csv")

################################# enhanced volcano###########################
library(ggplot2)
library(ggrepel)
library(EnhancedVolcano)
EnhancedVolcano(final_without_dots,
                lab = final_without_dots$X2,
                x = "log2FoldChange",
                y = "pvalue",
                pCutoff = 0.05,
                FCcutoff = 1.5,
                title = "MELANOMA VS NORMAL")





