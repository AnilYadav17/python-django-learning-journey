import numpy as np
a = np.array([10, 20, 30, 40, 50])
# print(a)
# for i in a:
#     print(i)

result = np.where(a>30)
print(result)