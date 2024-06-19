
import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "hisat2"
indices = "~/indices/grch38/genome"
option_SE = "-U"
input_dir = "/home/bcd/057/glore/"
output_sam_dir = "/home/bcd/057/mapping/sam/"
output_sorted_sam = "/home/bcd/057/mapping/sam_sorted/"
output_bam = "/home/bcd/057/mapping/bam/"
cores = " -p 4"


for x in accessions:
   
    command = inst_dir + cores + " " + "-x " + indices + " " + " -1 "  + input_dir + x + "_1_val_1.fq.gz" + " " + " -2 "  + input_dir + x + "_2_val_2.fq.gz" + " -S " + output_sam_dir + x + ".sam" + " " + "--un " + x + "_non_aligned.sam" + " _summary.txt" + x + "_summary.txt" + " -dta"
    print(command + " ....running....")
    os.system(command)
    command = "samtools sort" + " -o " + output_sorted_sam + x + "_sorted.sam " + output_sam_dir + x + ".sam"
    print(command)
    os.system(command)
    command = "samtools view" + " -bS " + output_sorted_sam + x + "_sorted.sam" " > " + output_bam + x + ".bam"
    print(command)
    os.system(command)


print("All done")
