
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
b[1,1]=10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)