
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "hisat2"
indices = "/media/bushra/NGS/TNER/hisat/hisat_grch38/genome"
option_SE = "-U"
input_dir = "/media/bushra/NGS/TNER/trim/"
output_sam_dir = "/media/bushra/NGS/TNER/sam/"
cores = " -p 12 "


for x in accessions:
   
    command = inst_dir + cores + "-x " + indices + " -U " + input_dir + x + "_trim.fastq.gz" + " -S " + output_sam_dir + x + ".sam" + " --un " + output_sam_dir + x + "_non_aligned.sam" + " --summary-file " + x + "_summary.txt" + " -dta"
    print(command + " ....running....")
    os.system(command)


print("All done")
