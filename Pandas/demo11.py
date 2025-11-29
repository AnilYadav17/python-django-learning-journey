#map with numeric data
import pandas as pd
a=pd.Series([11,12,13,14,15])
res=a.map(lambda x:x**2)
print(res)