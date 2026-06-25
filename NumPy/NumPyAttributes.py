import numpy as np

a1 = np.array([1,2,3])
print(a1)

a2 = np.arange(1,10).reshape(3,3)
print(a2)

print(a1.ndim) # number of dimensional
print(a2.shape) # (3, 3)
print(a2.size) # 3*3 = 9

print(a1.itemsize) # har item memory me kitna size lera hai output - 8 64 me default
print(a2.dtype) # int64
