#sort_index() in Series
import pandas as pn
data=pn.Series([100,200,50],index=[2,1,3])
res=data.sort_index()
res=data.sort_values(ascending=False)
print(res)