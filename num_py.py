# Numpy

# numpy is faster than list
# homogeneous data
#
# import numpy
# print(numpy.__version__)

import numpy as np
# print(np.__version__)
#
# x = np.array(10)   #Zero dimession
# print(x)
#
# x1 = np.array([10,1,2,3])    #single dimenssion
# print(x1)
#
# x2 = np.array([1,3],[4,6])
# print(x2)

# x3 = np.array([[[1,2,3],[4,5,6],[1,5,7]]])
# print(x3)
# print(x3.shape)

x4 = np.array([[[1,2],[1,3],[1,4],[4,6]]])
print(x4)
print(x4.shape)

print(x4.size)