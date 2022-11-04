import pandas as pd
import glob

all_files = glob.glob('mit/csv/*.csv')
li_mapper = map(lambda f:pd.read_csv(f,index_col=None,header=0),all_files)

li = list(li_mapper)
i = 0
for f in all_files:
    df = pd.read_csv(f,index_col=None,header=0)
    li.append(df)
df = pd.concat(li,axis=1,ignore_index=True)
print(df)