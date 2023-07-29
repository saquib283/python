import numpy as np
np.random.seed(111)
a=np.random.randint(1,500,56).reshape(7,8)
print(a)
# [start(row):end(n-1)(row),start0-(col):end(n-1)(col)]
print(a[2:4,4:6])