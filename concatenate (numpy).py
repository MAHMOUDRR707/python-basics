import numpy as np
z=np.array([1,2,3])
y=np.array([1,2,3])
x=np.array([1,2,3])
print(np.concatenate((x,y,z),axis=0))
print(np.concatenate((x,y,z),axis=1))
