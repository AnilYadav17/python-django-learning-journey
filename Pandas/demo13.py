import pandas as pd
data={
    "a":[1,2,3,],
    "b":[10,20,30],

}
df=pd.DataFrame(data)
maxdata=df.apply(lambda x:x.max())
print(maxdata)

total=df.apply(lambda x:x.min())
print(total)