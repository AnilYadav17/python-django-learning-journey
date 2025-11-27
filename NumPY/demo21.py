import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# COPY: Owns the data
c = arr.copy()
c[0] = 99
print("\n--- After modifying COPY (c[0]=99) ---")
print("Copy:", c)
print("Original:", arr, "(Unchanged)")

# VIEW: Does not own the data (looks at original)
v = arr.view()
v[1] = 88
print("\n--- After modifying VIEW (v[1]=88) ---")
print("View:", v)
print("Original:", arr, "(Changed!)")

# Checking ownership
print("\n--- Ownership Check ---")
print("Copy owns data?", c.base is None)
print("View owns data?", v.base is None)