import pandas as pd
import numpy as np
import math
loc_file = "/Users/wus19/Desktop/project/smartcity/location/location.xlsx"
data_file = "/Users/wus19/Desktop/project/smartcity/dataset/csv/marine_1986.csv"
rt_file="/Users/wus19/Desktop/project/smartcity/location/redtide.xlsx"
loca = pd.read_excel(loc_file, header=0).dropna()
redtide=pd.read_excel(rt_file,header=0)
# dict = {'中层', '底层'}
# data = pd.read_csv(data_file, header=0)
# data1 = []
# for i in range(len(data.iloc[:, 0]) - 1):
#     if data.iloc[i, 4] not in dict:
#         data1.append(data.iloc[i, :])
# label = pd.DataFrame(data1).iloc[:, :5]
# value = pd.DataFrame(data1).iloc[:, 5:]
# value.fillna((value.mean()), inplace=True)
# data2 = pd.concat([label, value], axis=1)
# data2.to_csv("/Users/wus19/Desktop/test.csv")
loc1=loca.loc[:,['水质监测站','经度','纬度']].values
loc2=redtide.loc[:,['红潮报告编号','报告日期','消退日期','组别','品种','位置','经度','纬度','座标系统']].values
#选取红潮位置和水质监测点坐标
latitude1=loc1[:,2]
longitude1=loc1[:,1]
latitude2=loc2[:,7]
longitude2=loc2[:,6]
#计算红潮和座标系统的长度
leng1=len(latitude1)-1
leng2=len(latitude2)-1
for i in range(leng2):#对红潮位置信息从i=0开始遍历，i=0，......leng1
    temp=[]#用于存放每组遍历的距离结果
    for j in range(leng1):#计算ith红潮信息与jth水质检测座标系统的距离，j=0....leng2
        temp.append(math.sqrt((longitude2[i]-longitude1[j])**2+(latitude2[i]-latitude1[j])**2))#计算euclid distance
    mini=min(temp)#找最小值
    index=temp.index(mini)#找最小值的下标
    loc2[i,5]=loc1[index,0]#用位置信息来储存最近的水质检测座标点
    loc2[i,8]=mini#用座标系统存储最近距离
distance=pd.DataFrame(loc2,columns=['红潮报告编号','报告日期','消退日期','组别','品种','最近水质监测点','经度','纬度','最近水质检测点距离'])
distance.to_csv('/Users/wus19/Desktop/min_location.csv',index=False)
# print(distance)
print('Finish')
