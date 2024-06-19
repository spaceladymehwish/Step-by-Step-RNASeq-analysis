
import os
##using ensembl genome through ftp for indices

file = open("ftp-links or ACC.txt")
accessions = file.read()
accessions = accessions.split()


inst_dir = "wget "



for x in accessions:
   
    command = inst_dir + x
    print(command + " ....running....")
    os.system(command)


print("All done")
