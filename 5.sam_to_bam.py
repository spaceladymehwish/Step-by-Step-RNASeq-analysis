
open terminal in melanoma rna seq, alignment folder

samtools view -S -b SRR14753170.sam -O or > ~/Desktop/melanome_RNASeq/Alignment/bam/SRR14753170.bam

to check for the usage of a tool simply type name of tool and press enter in command line

import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "samtools view"
input_dir = "~/Desktop/melanoma_RNASeq/Alignment/sorted/"
output_bam = "~/Desktop/melanoma_RNASeq/Alignment/bam/"
cores = " --threads 14 "


for x in accessions:
   
    command = inst_dir + cores + "-bS " + input_dir + x + "_sorted.sam" " > " + output_bam + x + ".bam"
    print(command)
    os.system(command)


print("All done")
