#for create a data  fram
import pandas as pd
data={
    "name":["ram", "anu","dipanshu"],
    "age":[10,12,11],
    "city":["indore","bhopal","ratlam"]
}
res=pd.DataFrame(data)
print(res)

