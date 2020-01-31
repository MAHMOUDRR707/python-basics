import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[1,2],[3,4]])
print(np.outer(a,b))
#[1,2,3,4], [2,4,6,8] , [3,6,9,12] ,[4,8,12,16]
a=np.array([1,2])
b=np.array([3,4])
print(np.outer(a,b))
#[3,4],[6,8]
