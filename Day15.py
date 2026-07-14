import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# A = np.array([
#     [0, 1, 0],
#     [0, 1, 1],
#     [0, 1, 0]
# ])
# B = np.array([
#     [0, 1, 0],
#     [0, 1, 1],
#     [0, 1, 0]
# ])
# print(A+B, "\n")
# print(A-B,"\n")
# result = np.dot(A, B)
#
# I = np.eye(3)
# print(I)
#
# Z = np.zeros((3,3))
# d = np.diag([1,2,3])

# Excercise
# 1)manipulation of matrix
# A = np.array([[1,2],[3,4]])
# B = np.array([[9,8],[7,6]])
# print(A+B,"\n")
# print(A-B,"\n")
# print(A*2*B)

# 2)implementing matrix multiplication
# M = np.array([[1,2,3],[4,5,6],[7,8,9]])
# v = np.array([1,2,3])
# result = np.dot(M, v)
# print(result)

# 3)Special Matrices
I = np.eye(4)
print(I)
D = np.diag([1,2,3])
print(D)
z = np.zeros((4,4))
print(z)
