import numpy as np
mark=np.array([72,85,49,90,67,55,38,76,81,60,45,88])
print("Shape: ",mark.shape)
print("Dimention: ",mark.ndim)
print("Datatype: ",mark.dtype)
print("Mean: ",np.mean(mark))
print("Maximum value: ",np.max(mark))
print("Minimum: ",np.min(mark))
print("Standard deviation: ",np.std(mark))
X=mark>=60
print("Marks more than 60: ",mark[X])
Y=mark<50
print("Marks less than 50: ",np.count_nonzero(Y))
z=mark.reshape(3,4)
print("Matrix form: ",z)
print("Sum of rows: ",np.sum(z,axis=1))

