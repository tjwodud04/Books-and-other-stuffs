import numpy as np

W = np.arange(21).reshape(7,3)
print(W)
print()
print(W[2])
print()
print(W[5])
print()

idx = np.array([1,0,3,0])
print(W[idx])

'''
결과
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]
 [12 13 14]
 [15 16 17]
 [18 19 20]]

[6 7 8]

[15 16 17]

[[ 3  4  5]
 [ 0  1  2]
 [ 9 10 11]
 [ 0  1  2]]
'''