#Create a 5x5 NumPy array with values ranging from 1 to 25 in a spiral pattern.

import numpy as np

def create_spiral(n):
    # initialize the matrix with zeros
    matrix = np.zeros((n, n))

    # define the value to be filled
    value = 1

    # define the boundaries
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while True:
        if left > right:
            break

        # fill the top row
        for i in range(left, right + 1):
            matrix[top, i] = value
            value += 1
        top += 1

        if top > bottom:
            break

        # fill the right column
        for i in range(top, bottom + 1):
            matrix[i, right] = value
            value += 1
        right -= 1

        if left > right:
            break

        # fill the bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom, i] = value
            value += 1
        bottom -= 1

        if top > bottom:
            break

        # fill the left column
        for i in range(bottom, top - 1, -1):
            matrix[i, left] = value
            value += 1
        left += 1

    return matrix

# create a 5x5 spiral matrix
print(create_spiral(5))
