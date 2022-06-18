#Find the sum of maximum and minimum value in the given numpy array
# and find mean and standard deviation
import numpy as np
c = np.array([-10, 201, 43, 94, 502])

c_max = c.max()
print("c_max is: ", c_max)
c_min = c.min()
print("c_min is: ", c_min)
c_sum = c_max + c_min
print("sum of max and min is : ",c_sum)
c_mean = c.mean()
c_std = c.std()
print("mean is: ", c_mean, "standard deviation is: ",c_std)
