import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# print("Determinant:", np.linalg.det(a))
#
# print("\nEigenvalues and Eigenvectors:")
# values, vectors = np.linalg.eig(a)
# print("Eigenvalues:", values)
# print("Eigenvectors:\n", vectors)
#
# try:
#     inverse = np.linalg.inv(a)
#     print("\nInverse:\n", inverse)
# except np.linalg.LinAlgError:
#     print("\nMatrix is singular. Inverse does not exist.")

# U, S, V = np.linalg.svd(a)
# print("\nU:\n", U)
# print("\nS:\n", S)
# print("\nV:\n", V)

# Excercise :
# A = np.array([[2,3,1],
#               [4,1,2],
#               [1,5,3]])
# determinant = np.linalg.det(A)
# inverse = np.linalg.inv(A)
# print(determinant,"\n")
# print(inverse,"\n")

# compute eigen value and vector
# a = np.array([[4,-1],[1,1]])
# eigenval , eigenvec = np.linalg.eig(a)
# print(eigenval)
# print(eigenvec)

# SVD
A = np.array([[1,2,3],[-1,3,1],[1,1,3]])
u , s , v = np.linalg.svd(A)
print(u,"\n")
print(v,"\n")
print(A,"\n")
# Reconstruct
sigma = np.zeros((3,3))
np.fill_diagonal(sigma,s)
reconstruct = u @  sigma @ v
print(reconstruct)