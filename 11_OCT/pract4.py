# lst = [1, 2,3, 4, 5]
# lst.append(0)
# print(lst)


# tpl = tuple()
# tpl = (1, 2, 3, 5, 6)
# print(tpl)


# set1 = {1,3 , 3 ,5}
# set1.add(2)
# print(set1)

# dict1 = dict()
# dict2 = {0:0 , 1:1 , 2:2 ,10:10}
# for key in dict2:
#     print("Key :", key, " Value :", dict2[key])
    
# print("Value of key  0 :", dict2[0])


# print(
#     type(lst), type(tpl), type(set1), type(dict2)
# )


# lst1 = [4, 5, 8, 6, 4, 2, 8, 1, 0, 7]
# print("LST1  :",lst1)
# search = float(input("Enter element to search in LST1 :"))

# temp = 0
# for i in range(0, len(lst1)):
#     if(lst1[i] == search):
#         print("Element found at indexx ",i, " and position ", i+1 )
#         break
# else:
#     print("Element not found in LST1")


# tpl = (2, 5, 6, 1, 7, 6, 8)
# print(tpl)
# lst = list(tpl)
# lst.sort(reverse=True)
# tpl1 = tuple(lst)
# print(lst)  #both of the output will going tobe same s they are  same , we just change the type form list to tuple
# print(tpl1)



# 🐍 Exploring important functions and variables of sys module

# import sys

# print("=== System Info ===")
# print("Python Version:", sys.version)                # shows full version info
# print("Python Version Info:", sys.version_info)      # shows version as tuple (major, minor, micro)
# print("Platform:", sys.platform)                     # OS info (win32, linux, etc.)
# print("Executable Path:", sys.executable)            # Python interpreter path

# print("\n=== Memory & Object Info ===")
# a = 100
# print("Value of a:", a)
# print("Memory Size of a:", sys.getsizeof(a), "bytes")  # returns memory size
# print("Unique ID of a:", id(a))                        # memory address

# print("\n=== Module Info ===")
# print("Loaded Modules Count:", len(sys.modules))      # total modules loaded
# print("Some Modules:", list(sys.modules.keys())[:5])  # first 5 module names

# print("\n=== Command Line Arguments ===")
# print("Arguments passed to script:", sys.argv)        # shows arguments (if run from terminal)

# print("\n=== Path Info ===")
# print("Search Paths for Modules:")
# for p in sys.path:                                    # shows where Python searches for modules
#     print("  ", p)

# print("\n=== Standard Streams ===")
# print("Standard Input Object:", sys.stdin)
# print("Standard Output Object:", sys.stdout)
# print("Standard Error Object:", sys.stderr)

# print("\n=== System Limits ===")
# print("Max Recursion Limit:", sys.getrecursionlimit())  # max recursion depth
# print("Max Integer Size:", sys.maxsize)                 # largest integer supported

# # Optional exit
# # print("\nNow exiting program safely...")
# # sys.exit("Goodbye! Program terminated by sys.exit()")



import sys
print(sys.version)
a = 10 
print(sys.getsizeof(a))
print(id(a))
print(sys.maxsize)
