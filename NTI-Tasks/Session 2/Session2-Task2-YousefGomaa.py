# # Yousef Ibrahim Gomaa Mahmoud

# # Exercise 1 Q1
import numpy as np

# # 1.
mat = np.random.rand(2)

print("Matrix",mat)
print("Min:",np.min(mat),"\nMax",np.max(mat))

# # 2.
mat2 = np.random.randn(20)
print("\n1-Dimensional:",mat2)

mat2 = mat2.reshape(4,5)

print("\n2-Dimensional 4x5:",mat2)

# # Exercise 2 Q2

arr = np.array([[1,  6, 11], [2,  7, 12], [3,  8, 13],
 [4,  9, 14], [5, 10, 15]])

new_arr = np.array([list(arr[1]),list(arr[3])])

print("Array:",arr)
print("New Array \"2nd Row and 4th Row\":",new_arr)

# # Exercise 3 Q3

arr = np.random.rand(100)

print("Mean:",np.mean(arr),"\nMedian:",np.median(arr),"\nStandard Deviation:",np.std(arr))

arr =10*np.random.rand(5,5)
print("Array:",arr)

arr = (arr - np.mean(arr)) / np.std(arr)
print("Normalized:",arr)

# # Exercise 4 Q4
arr = np.random.rand(3,3)
print("Array:",arr)

arr = np.transpose(arr)
print("Transposed:",arr)

arr1 = np.random.rand(3,4)
arr2 = np.random.rand(4,3)
print("Array 1:",arr1)
print("Array 2:",arr2)
print("Multiplication:",np.matmul(arr1,arr2))

arr = np.random.rand(3,3)
print("Array:",arr)
print("Determinant:",np.linalg.det(arr))
print("Inverse:",np.linalg.inv(arr))
