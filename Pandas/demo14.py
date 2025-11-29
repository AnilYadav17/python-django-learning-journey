import pandas as pd
data={
    "a":[1,2,3,],
    "b":[10,20,30],

}
df=pd.DataFrame(data)
print(df)
res1=df.apply(lambda x:x.max()-x.min(),axis=0)
print(res1)
res2=df.apply(lambda x:x.max()-x.min(),axis=1)
print(res2)