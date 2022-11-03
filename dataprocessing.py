import numpy as np
import pandas as np
import pandas as pd
from data import  processing
import os
import csv

path='/Users/wus19/Desktop/project/smartcity/dataset/'
target='/Users/wus19/Desktop/project/smartcity/xlsx/'

if not os.path.exists(target):
    os.makedirs(target)
files=os.listdir(path)
pre=processing()
for file in files:
    if  '.DS_Store' not in file:
        paths=os.path.join(path,file)
        if os.path.isfile(paths):
            x=pre.filna(paths)
            s=pd.DataFrame(x)
            target_path=os.path.join(target,file)
            if os.path.exists(target_path):
                os.remove(target_path)
            s.to_excel(target_path,index=False)
print('Finish!')
