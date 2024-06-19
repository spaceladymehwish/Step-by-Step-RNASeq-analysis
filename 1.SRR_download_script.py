#Accessing fastq files stored in SRR14753170 ID

#Open terminal in ~/Downloads/sratoolkit.3.0.2-ubuntu64$

  ~/Downloads/sratoolkit.3.0.2-ubuntu64/bin/./fastq-dump --split-3 --origfmt --gzip -O ~/Desktop/melanoma_RNASeq/RAW/ SRR14753170



import os


file = open("acc.txt") #accessions text file
accessions = file.read()
accessions = accessions.split()


inst_dir = "~/Downloads/sratoolkit.3.0.2-ubuntu64/bin/./fastq-dump" #installation folder of sratoolkit/fastq-dump
paired_split = "--split-3" #only for paired end data, if single end -- remove this option from the command below
fmt = "--origfmt"
outfmt = "--gzip"
output_dir = "-O ~/Desktop/melanoma_RNASeq/RAW/" #output folder, carefully enter the aboslute address

for x in accessions:
   
    command = inst_dir + " " + paired_split + " " + fmt + " " + outfmt + " " + output_dir + " " + x #make sure if data is paired/single
    print(command + " ....running....")
    os.system(command)
    print("All done")
