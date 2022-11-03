import pandas as pd
import numpy as np
class processing():
    def filna(self,file):
        dict = {'中层', '底层'}
        data = pd.read_excel(file, header=0)
        data1 = []
        for i in range(len(data.iloc[:, 0]) - 1):
            if data.iloc[i, 4] not in dict:
                data1.append(data.iloc[i, :])
        label = pd.DataFrame(data1).iloc[:, :5]
        value = pd.DataFrame(data1).iloc[:, 5:]
        value.fillna((value.mean()), inplace=True)
        data2 = pd.concat([label, value], axis=1)
        return data2

