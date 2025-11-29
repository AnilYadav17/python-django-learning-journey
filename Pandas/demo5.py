#for create data frame
import pandas as pd
data = {
      'Name': ['Aniket', 'Biku', 'Jatin', 'Anurag'],
      'Age': [23, 22, 21, 24],
      'City': ['Pune', 'Mumbai', 'Delhi', 'Bangalore']}
res = pd.DataFrame(data)
#print(res["City"])
#print(res["Name"])
#print(res["Age"])
print(res['Age']>11)


