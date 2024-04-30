# 8. Solve the system of linear equations 2x + 3y = 7 and x - y = 1 using NumPy's linear algebra functions.

import numpy as np

# coefficients of the equations
A = np.array([[2, 3], [1, -1]])

# constants on the right side
b = np.array([7, 1])

try:
    # solve the system of equations
    solution = np.linalg.solve(A, b)
    print(f"The solution is x = {solution[0]} and y = {solution[1]}")
except np.linalg.LinAlgError:
    print("!!!The system of equations does not have a unique solution.")
