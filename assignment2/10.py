# Create a 5x5 NumPy array filled with the square of the numbers from 1 to 25 using broadcasting
import numpy as np

# create an array of numbers from 1 to 25
numbers = np.arange(1, 26)

# reshape the array to a 5x5 matrix
numbers = numbers.reshape((5, 5))

# square each number in the matrix using broadcasting
squared_numbers = numbers ** 2

print(squared_numbers)
