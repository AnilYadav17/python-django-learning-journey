import numpy  as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([60, 70, 80, 90, 100])
c = np.vstack((a,b))
print(c)

d = np.hstack((a,b))
print(d)