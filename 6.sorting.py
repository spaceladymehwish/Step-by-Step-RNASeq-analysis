open terminal in melanoma_RNASeq folder, goto alignment then open bam folder 

samtools sort --threads 12 SRR14753170.bam -O or > ~/Desktop/melanoma_RNASeq/Alignment/sorted/SRR14753170_sorted.bam 

import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "samtools sort"
input_dir = "~/Desktop/melanoma_RNASeq/Alignment/sam/"
output_sorted_sam = "~/Desktop/melanoma_RNASeq/Alignment/sorted/"
cores = " --threads 14 "


for x in accessions:
   
    command = inst_dir + cores + input_dir + x + ".sam" + " -o " + output_sorted_sam + x + "_sorted.sam"
    print(command)
    os.system(command)
    


print("All done")
