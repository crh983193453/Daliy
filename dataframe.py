import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

data={
        '姓名':['张一','张二','张三','张四','张五','张六'],
        '性别':['男','男','男','男','男','男'],
        '体重':[60,51,48,71,58,96],
        '年龄':[1,2,3,4,5,6],
        '分数':[1,2,3,4,5,6],
        '出生年月':['2000','2000','2000','2000','2000','2000'],
}
print(DataFrame(data).size)
print(DataFrame(data).ndim)
print(DataFrame(data).shape)
df=pd.DataFrame(data)
print(plt.plot(df['体重'],df['年龄']))
print(plt.bar(df['姓名'],df['分数']))