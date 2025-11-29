#reindex on dataframe

import pandas as pd
data=pd.DataFrame({"a":[1,2,3,4,5],"b":[10,20,30,40,50]}, index=["a", "b", "c", "d", "e"])
print(data)
