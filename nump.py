import numpy as np

a = np.array([1,2,3,4,5])
print(a)
print(a[2])
print(a[1:])
print(a[1:4])
print(a[-2])
print(a[:-2])
a[3] = 10
print(a[-2:])
#same as python list
a_mul = np.array([[1,2,3,4],
                 [4,4,5,6],
                 [1,2,3,4]])
               
print(a_mul[0])
print(a_mul[0,1])
print(a_mul.shape)
a1 = np.array([[[1,2,3,4],
                [2,3,4,5],
                [3,4,5,6]],
                [[9,8,7,6],
                 [8,7,6,5],
                 [7,6,5,4]]])
# print(a1[0])
print(a1.shape)
print(a1.ndim)
print(a1.size)
q1 = np.array([5,6,7])
print(q1.dtype)
q2 = np.array([1,3,"5"])
print(q2.dtype)
q3 = np.array([1,2,"5"],
               dtype = np.int32)
print(q3.dtype)
ax = np.full((2,3,4),10)
print(ax)
ax = np.empty((2,3))
print(ax)
ax = np.arange(0, 1001, 10)
print(ax)
ax = np.linspace(0, 1000, 5)
print(ax)
print(np.sqrt(-1))
print(np.array([10])/0)
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5)
print(a1 * 5)
print(l1 + l2)
print(a1 + a2)

a1 = np.array([1,2,3])
a2 = np.array([[1],
               [2]])
print(a1 + a2)

a1 = np.array([1,2,3])
a1 = np.append(a1, [7, 8, 9])
print(a1)
a1 = np.insert(a1, 3, [4,5,6])
print(a1)


a = np.array([[1,2,3,4],
               [4,5,6,7]])
b = np.array([[8,9,10,11],
               [15,14,13,12]])
print(np.delete(a, 2, 1))

var1 = a.ravel()
var1 = a.ravel()
var1[2] = 50
print(a)
print(var1)
print(a.T)
print(a.swapaxes(0,1))

a = np.concatenate((a, b), axis=1)
print(a)

a = np.array([[1,2,3,4],
               [4,5,6,7],
               [8,9,10,11],
               [15,14,13,12]])
# print(np.split(a, 2, axis = 1))
print(a.min(),a.max(), a.mean())
print(np.median(a))

n1 = np.random.randint(100, size=(2, 3, 4))
print(n1)

n1 = np.random.binomial(10, p = 0.5, size=(2,3,3))
print(n1)

n1 = np.random.normal(loc=170, scale=15, size=(5,2))
print(n1)

n1 = np.random.choice([10, 11, 12, 13])
print(n1)