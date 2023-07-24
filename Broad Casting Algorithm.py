import numpy as np
v = np.array([12,24,36])
w = np.array([45,55])
print(np.reshape(v,(3,1))*w)
x = np.array([[12,22,33],[45,55,66]])
print(x+v)
print(((x.T)+w).T)
print(x*2)
