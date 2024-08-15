# # Yousef Ibrahim Gomaa Mahmoud
# # Task 1
# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# input = "Hello"
# num_vowels = count_vowels(input)
# print("Number of vowels:", num_vowels)

# # Task 2
# def count_iti(input):
#     count = 0
#     while True:
#         test = input.find("iti")
#         if test > -1:
#             count = count+1;
#             input = input[test+3:]
#             continue
#         else:
#             break
#     return count

# print("Number of \"iti\" in string:",count_iti("Hello, welcome to iti, iti is the best."))

# # Task 3
# def remove_vowels(string):
#     vowels = "aeiouAEIOU"
#     newString = ""
#     for char in string:
#         if char not in vowels:
#             newString = newString+char
#     return newString

# input = "Hello"
# print("String:",input,"- Removed Vowels:",remove_vowels(input))

# # Task 4
import numpy as np

mat = np.random.rand(2)

print(mat)
print("Min:",np.min(mat),"\nMax",np.max(mat))

# # Task 5
mat2 = 0+1*np.random.randn(20)
print("\n1-Dimensional:",mat2)

mat2 = mat2.reshape(4,5)

print("\n2-Dimensional 4x5:",mat2)