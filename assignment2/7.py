# Given a NumPy array, 
# find the indices of the minimum and maximum elements, and swap those elements without affecting the rest of the array.

import numpy as np

def swap_min_max(arr):
    # find the index of the minimum element
    min_index = np.argmin(arr)
    # find the index of the maximum element
    max_index = np.argmax(arr)
    
    # store the minimum and maximum elements in temporary variables
    min_val, max_val = arr[min_index], arr[max_index]
    
    # swap the minimum and maximum elements
    arr[min_index], arr[max_index] = max_val, min_val
    
    return arr

arr = np.array([6,7,23,4,67,5]) #example array taken
print("Modified array is :",swap_min_max(arr)) #function called
