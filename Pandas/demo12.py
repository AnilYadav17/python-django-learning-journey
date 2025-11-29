#apply with data frame
import pandas as pd
data={
     "a":[1,2,3],
     "b":[10,20,30]

}
df=pd.DataFrame(data)
#df["a"]=df["a"].apply(lambda x:x*2)
#df["b"]=df["b"].apply(lambda x:x+2)
#print(df["a"])
#print(df["b"])
'''result=df.apply(sum,axis=0)
print(result)'''

#for coloum sum
#colsum=df.apply(lambda x:x["a"]+x["b"],axis=1)
#print(colsum)

#for applymap
res=df.applymap(lambda x:x*2.max())
print(res)
