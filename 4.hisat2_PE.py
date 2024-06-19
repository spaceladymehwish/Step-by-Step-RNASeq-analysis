
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "hisat2"
indices = "~/Desktop/melanoma_RNASeq/indices/indices_reference_genome"
input_dir = "~/Desktop/melanoma_RNASeq/trim/"
output_sam_dir = "~/Desktop/melanoma_RNASeq/Alignment/"
summary_file = "~/Desktop/melanoma_RNASeq/Alignment/summary/"
cores = " -p 12"


for x in accessions:
   
    command = inst_dir + cores + " " + "-x " + indices + " -1 "  + input_dir + x + "_trim_1.fastq.gz" + " -2 " + input_dir + x + "_trim_2.fastq.gz" + " -S " + output_sam_dir + x + ".sam" + " " + " --summary-file " + summary_file + x + "_summary.txt" + " --dta "
    print(command + " ....running....")
    os.system(command)
    


print("All done")
