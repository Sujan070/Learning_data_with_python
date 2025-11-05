import numpy as np
import numpy.ma as ma
a = np.array([2, 3, 4])
b = np.array([4])

a = np.array([1, 3, 4])
b = np.array([[4], [5]])

a = np.random.random((5, 3, 4, 1, 2, 1))
b = np.random.random((5, 1, 4, 7, 2, 6))
print((a+b).shape)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[0:4])
print(a[0:9:2])

a = np.random.random((3,3))
print(a)
print(a[[0,2]])
print(a[[0,2],np.newaxis])

a = np.array([[6, 5, 1],
              [3, 7, 1,],
              [9, 5, 7]])
print(np.sort(a))
print(np.sort(np.sort(a,axis=1),axis=0))

out = np.array([0.05, 0.23, 0.66, 0.764, 0.322,0.245 ])
print(np.argmax(out))

a = np.arange(12).reshape(4, 3)
print(a)

for elm in np.nditer(a):
    print(elm, end=" ")

for elm in np.nditer(a, order="F"):
    print(elm, end=" ")

with np.nditer(a, op_flags=["readwrite"]) as it:
    for elm in it:
      elm[...] = elm + 5
print(a)

arr = np.array([1, 2, 3, np.nan, np.inf])
print(arr.mean())
masarr = ma.masked_array(arr, mask = [0, 0, 0, 1, 1])
print(masarr.mean())

a = np.array([1, 2, 3, 4, 5, 6])
varr = a[0:4]
print(varr.base)

varr = a.copy()
print(varr.base)


a = np.array([[6, 5, 1],
              [3, 7, 1,],
              [9, 5, 7]])

b = np.array([[3, 5, 1],
              [3, 7, 1,],
              [9, 8, 7]])
print(np.matmul(a, b))
print(a @ b)

def plus2 (x):
    x += 2
    return x
vec_plus2 = np.vectorize(plus2)
print(vec_plus2(a))
