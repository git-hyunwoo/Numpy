import numpy as np

print(f"np.__version__ : {np.__version__}")

l = [[1,2,3], [4,5,6]]
print(f"type(l) : {type(l)}")

for i in dir(np.ndarray):
    if not i.startswith("__"):
        if type(np.ndarray.__dict__[i]) != type(np.ndarray.var):
            print(i)