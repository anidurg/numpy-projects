#Task: Creating Horizontal and vertical Vectors in numpy
import numpy as np
#create a 1-D list(horizontal)
list1 = [1,2,3]

#create a 1-D list(vertical)
list2 = [[10],[20],[30]]

#creating a vector 1. vector as a row
vector1 = np.array(list1)
#creating a vector 1. vector as a row
vector2 = np.array(list2)

#print
print("Horizontal vector")
print(vector1)
print("------*******--------*******------")
print("Vertical vector")
print(vector2)
