import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[1,2],[3,4]])
print(np.dot(a,b))
#[[1*1+2*3, 1*2+2*4],[3*1+4*3, 3*2+4*4]]
a=np.array([1,2])
b=np.array([3,4])
print(np.dot(a,b))
# 1*3+2*4
print(a*b)
#[3,8]

