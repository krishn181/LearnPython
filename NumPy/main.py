import numpy as np

a = np.array([1,2,3,4])
print(a)
print(type(a))

b = np.array([[1,2,3,4],[1,2,3,4]])
print(b)
print(type(b))

c = np.array([['hello','world'],['new','numpy']], dtype=str)
print(c)
print(type(c))

d= np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
print(d)

r_eshape = np.arange(1,11).reshape(5,2)# (row, clm)
print(r_eshape)

np_one = np.ones((1,3))
print(np_one)

np_zero = np.zeros(())
np_linspace = np.linspace(-10,10,10) #
print(np_linspace)

np_identity = np.identity(3)
print(np_identity)