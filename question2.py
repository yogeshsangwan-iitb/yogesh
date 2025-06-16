import numpy as np
import random

arr = np.array([random.uniform(0, 10) for i in range(20)])
arr = np.round(arr, 2)
print("Original Array (rounded):")
print(arr)

print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Median:", np.median(arr))

new_arr = []
for val in arr:
    if val < 5:
        new_arr.append(round(val ** 2, 2))
    else:
        new_arr.append(val)
new_arr = np.array(new_arr)
print("Modified Array (squared if < 5):")
print(new_arr)

def numpy_alternate_sort(array):
    sorted_arr = np.sort(array)
    left = 0
    right = len(sorted_arr) - 1
    result = []
    while left <= right:
        result.append(sorted_arr[left])
        left += 1
        if left <= right:
            result.append(sorted_arr[right])
            right -= 1
    return np.array(result)

alt_sorted = numpy_alternate_sort(new_arr)
print("Alternately Sorted Array:")
print(alt_sorted)
