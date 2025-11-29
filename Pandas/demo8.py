#describe() on Data Frame
import pandas as pd
data={
    "age":[10,20,22],
    "marks":[100,150,170],
}
df=pd.DataFrame(data)
print(df["age"].mean())
print(df["age"].median())
print(df["age"].mode())
print(df["age"].std())
print(df["age"].var())
print(df["age"].min())
print(df["age"].max())
print(df["age"].sum())
print(df["age"].count())



