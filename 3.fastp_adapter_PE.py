
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "fastp"
seq_dir = "~/Desktop/Kidney_miRNA/E-GEOD-24457/Raw/sequences/"
input_dir = "~/Desktop/Kidney_miRNA/E-GEOD-24457/Raw/"
output_dir = "~/Desktop/Kidney_miRNA/E-GEOD-24457/Trim/"
cores = " -w 12 "

for x in accessions:
   
    command = inst_dir + " --adapter_fasta " + seq_dir + x + ".fasta" + cores + "-i " + input_dir + x + "_1.fastq.gz" + " -I " + input_dir + x + "_2.fastq.gz" + " -o " + output_dir + x + "_trim_1.fastq.gz" + " -O " + output_dir + x + "_trim_2.fastq.gz"
    print(command + " ....running....")
    os.system(command)

print("All done")
