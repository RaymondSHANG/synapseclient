import synapseclient
import os
import pandas as pd
import sys
import datetime

# Read the bamFiles.txt to get all syn_numbers and the corresponding names
# filename = '/Users/yshang/ncbi/public/ROSMAP/RNASeq/bamFiles.txt'
# filenumber = int(sys.argv[1])
start_num = int(sys.argv[1])
end_num = int(sys.argv[2])
# filename = ''.join(['./bamFilesBatch', filenumber])
filename = str(sys.argv[3])

df = pd.read_csv(filename, sep='\t', header=(0))
allsyn = df['synID']
totalLength = len(allsyn)
# Set the login information
syn = synapseclient.Synapse()
upass = pd.read_csv(
    "~/Documents/mydoc/ampad_userpass.txt", header=None)
username, password = upass.iloc[0, 0].strip(), upass.iloc[0, 1].strip()


syn.login(username, password)

# Obtain a pointer and download the data
# tmpsyn = ('syn4212586','syn4212972','syn4212973')
# Easier test
# tmpsyn= ('syn3505724','syn4300315','syn4300317')
# tmpsyn = allsyn[start_num:(end_num+1)]
newFolder = df['path'][start_num]  # ''.join((str(start_num),"_",str(end_num)))
directory_current = os.path.join(os.getcwd(), newFolder)
if not os.path.exists(directory_current):
    os.makedirs(directory_current)
totalNumber = end_num-start_num+1
currentNumber = start_num
# Processing from start_num, to end_num
for currentNumber in range(start_num, end_num+1):
    syn_number = allsyn[currentNumber]
    print('starting:', (currentNumber+1), "/", totalLength,
          "(currentJobSize:", totalNumber, ")\n", syn_number, "...\n")
    syn_pointer = syn.get(entity=syn_number, downloadLocation=newFolder)
    # Get the path to the local copy of the data file
    # filepath = syn_pointer.path
    os.system('say "one file has finished"')
    print(syn_number, ":", syn_pointer.path, "\t Finished! \n")
    print(datetime.datetime.now(), "\n\n")
    syn_pointer = ()
