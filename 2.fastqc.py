for one sample 

 fastqc samplename.fastq.gz -O ~/Desktop/melanoma_RNASeq/QC/initial/

 or

for all samples

 fastqc *.fastq.gz 


import os
##using ensembl genome through ftp for indices

file = open("acc.txt")
accessions = file.read()
accessions = accessions.split()

inst_dir = "fastqc"
input_dir = "~/Desktop/melanoma_RNASeq/RAW/"
output_dir = "~/Desktop/melanoma_RNASeq/QC/initial/"

for x in accessions:
   
    command = inst_dir + " " + input_dir + x + "_trim.fastq.gz" + " -o " + output_dir
    print(command + " ....running....")
    os.system(command)

print("All done")
