#map with series
import pandas as pd
data=pd.Series(["abc","xyz","pqr"])
print(data)
result=data.map(lambda x:x.upper())
print(result)

