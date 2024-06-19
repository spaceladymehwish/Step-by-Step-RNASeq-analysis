cutadapt -a file:illumina_adapter -o ERR9659988.fastq.gz ERR9659988_trim.fastq.gz

for batch run, run the script but for simgle sample use this command

fastp -w 12 -i sample_1.fastq.gz -I sample_2.fastq.gz -o ~/Desktop/melanoma_RNASeq/trim/sample_1_trim.fastq.gz -O ~/Desktop/melanoma_RNASeq/trim/sample_2_trim.fastq.gz

import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "fastp"
input_dir = "~/Desktop/melanoma_RNASeq/RAW/"
output_dir = "~/Desktop/melanoma_RNASeq/trim/"
cores = " -w 12 "

for x in accessions:
   
    command = inst_dir + cores + "-i " + input_dir + x + ".fastq.gz" + " -o " + output_dir + x + "_trim.fastq.gz"
    print(command + " ....running....")
    os.system(command)

print("All done")
