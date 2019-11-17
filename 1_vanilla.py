# %%
import numpy as np
import os
from numpy import genfromtxt
import time

# %%
#sizes = [2, 100, 1000, 2000, 5000, 10000]
sizes = [2, 100]

# %%
base_path='./test_data'

# %%
def matrix_mul_vanilla(A, B):
    res = [[0 for x in range(len(B[0]))] for y in range(len(A))]

    start = int(round(time.time() * 1000))
    for i in range(0, len(A)):
            for j in range(0, len(B[0])):
                for k in range(0, len(B)):
                     res[i][j] += A[i][k] * B[k][j]

    print("Time --->", (int(round(time.time() * 1000)) - start))
    return res

# %%


# %%
for size in sizes:
    file_A = 'A_' + str(size) + '.csv'
    file_B = 'B_' + str(size) + '.csv'
    path_A = os.path.join(base_path, file_A)
    path_B = os.path.join(base_path, file_B)
    print(path_A)
    print(path_B)
    A = genfromtxt(path_A, delimiter=',')
    B = genfromtxt(path_B, delimiter=',')
    res = matrix_mul_vanilla(A, B)

# %%
