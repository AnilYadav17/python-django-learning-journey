#for create data frame
import pandas as pd
data = {
      'Name': ['Aniket', 'Biku', 'Jatin', 'Anurag'],
      'Age': [23, 22, 21, 24],
      'City': ['Pune', 'Mumbai', 'Delhi', 'Bangalore']}
res = pd.DataFrame(data)
#print(res)


#print(res.head(2))   # for specified number of rows from top


print(res.tail(2))