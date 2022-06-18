#basic arithmetic operations
# importing numpy
import numpy as np

# creating a 1-D list (Horizontal)
list1 = [5, 6, 9]

# creating a 1-D list (Horizontal)
list2 = [1, 2, 3]

# creating first vector
vector1 = np.array(list1)

# printing vector1
print("First Vector : " + str(vector1))

# creating second vector
vector2 = np.array(list2)

# printing vector2
print("Second Vector : " + str(vector2))

# adding both the vector
# values of both the lists will be added corresponding to their indices
addition = vector1 + vector2

# printing addition vector
print("Vector Addition : " + str(addition))

# subtracting both the vector
subtraction = vector1 - vector2

# printing addition vector
print("Vector Subtraction : " + str(subtraction))

# multiplying  both the vector
multiplication = vector1 * vector2

# printing multiplication vector
print("Vector Multiplication : " + str(multiplication))

# dividing  both the vector
# my next task is to ensure that 0 should not be the divisor
division = vector1 / vector2

# printing division vector
print("Vector Division  : " + str(division))
