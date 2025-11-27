#sorting on 2D Array

import numpy as np 
a = np.array([[8,2 ,7, 5,4,8, 9],[1,2,3,4,5,6,7]])
print(a)

result = np.sort(a, axis=1)
print(result)