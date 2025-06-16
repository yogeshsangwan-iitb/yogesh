import random
import numpy as np

array = np.array([[random.randint(1, 50) for _ in range(4)] for _ in range(5)])
print("Original Array:\n", array)

anti_diag = [array[i, -1 - i] for i in range(min(array.shape))]
print("\nAnti-diagonal elements (top-right to bottom-left):", anti_diag)

row_max = np.max(array, axis=1)
print("\nMaximum value in each row:", row_max)

mean_val = np.mean(array)
filtered_array = array[array <= mean_val]
print(f"\nArray elements <= mean ({mean_val:.2f}):", filtered_array)

def numpy_boundary_traversal(matrix):
    rows, cols = matrix.shape
    boundary = []
    for j in range(cols):
        boundary.append(matrix[0, j])
    for i in range(1, rows):
        boundary.append(matrix[i, cols - 1])
    if rows > 1:
        for j in range(cols - 2, -1, -1):
            boundary.append(matrix[rows - 1, j])
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            boundary.append(matrix[i, 0])
    return boundary

boundary_elements = numpy_boundary_traversal(array)
print("\nBoundary elements (clockwise):", boundary_elements)
