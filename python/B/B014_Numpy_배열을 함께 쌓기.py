import numpy as np
import numpy.random as rg

# 배열을 함께 쌓기


a = np.floor(10 * rg.random((2, 2)))
print(a)

b = np.floor(10 * rg.random((2, 2)))
print(b)

print(np.vstack((a, b)))

print(np.hstack((a, b)))


from numpy import newaxis
print(np.column_stack((a, b)))  # with 2D arrays

a = np.array([4., 2.])
b = np.array([3., 8.])

print(np.column_stack((a, b)))  # returns a 2D array

print(np.hstack((a, b)))        # the result is different

print(a[:, newaxis])  # view `a` as a 2D column vector

print(np.column_stack((a[:, newaxis], b[:, newaxis])))

print(np.hstack((a[:, newaxis], b[:, newaxis])))  # the result is the same

print(np.column_stack is np.hstack)

print(np.row_stack is np.vstack)

print(np.r_[1:4, 0, 4])

