import numpy as np
import pandas as pd
df=pd.read_csv(r'D:\AI\第3章\data\data\used_cars.csv',sep=',',header=0)
columns=['brand','bodyType','fuelType','gearbox','power','kilometer','notRepairedDamage','days','v_0','v_1','price']
df=df[columns][:]
df=(df-df.min())/(df.max()-df.min())