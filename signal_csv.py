import wfdb 
import pandas as pd
import numpy as np
import glob
dat_files=glob.glob('mit/*.dat') 
df=pd.DataFrame(data=dat_files)
df.to_csv("mit/files_list.csv",index=False,header=None) #Write the list to a CSV file
files=pd.read_csv("mit/files_list.csv",header=None)
for i in range(1,len(files)):
	recordname=str(files.iloc[[i]])
	#print(recordname[:-4])
	recordname_new=recordname[-11:-4] 
	#print(recordname_new)#Extracting just the filename part (will differ from database to database)
	record = wfdb.rdsamp(recordname_new) # rdsamp() returns the signal as a numpy array  
	record=np.asarray(record[0])
	path="mit/csv/"+str(i)+".csv"
	np.savetxt(path,record,delimiter=",") #Writing the CSV for each record
	print("Files done: %s/%s"% (i,len(files)))

print("\nAll files done!")