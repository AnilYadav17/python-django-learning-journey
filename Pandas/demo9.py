#apply function on with dataframe
import pandas as pd
data={
    "a":([10,20,30,40,50]),

}
df=pd.DataFrame(data)
df["a"]=df.apply(lambda x:x+5   )
print(df)
