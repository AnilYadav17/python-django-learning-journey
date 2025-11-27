#concetanate the array
import numpy as np
a = np.array([[10, 20],[40, 50]])
print(a)

b=np.array([[60, 70],[90, 100]])
print(b)

c=np.concatenate((a,b), axis=0)
print(c)
