# %%
import numpy as np
import os
from numpy import genfromtxt
import time
from optparse import OptionParser

print('Vanilla Matrix Multiplication')

# %%
base_path='./test_data'

# %%
def matrix_mul_vanilla(A, B):
    res = [[0 for x in range(len(B[0]))] for y in range(len(A))]

    for i in range(0, len(A)):
            for j in range(0, len(B[0])):
                for k in range(0, len(B)):
                     res[i][j] += A[i][k] * B[k][j]
    return res

if __name__ == "__main__":
    parser = OptionParser()
    # takes size as an arg
    parser.add_option("-s",
                      dest="size",
                      default="2",
                      help="input matrix size")
    (options, args) = parser.parse_args()

    print('Matrix Size: {}'.format(options.size))
    size = options.size

    file_A = 'A_' + str(size) + '.csv'
    file_B = 'B_' + str(size) + '.csv'
    path_A = os.path.join(base_path, file_A)
    path_B = os.path.join(base_path, file_B)
    A = genfromtxt(path_A, delimiter=',')
    B = genfromtxt(path_B, delimiter=',')
    C = matrix_mul_vanilla(A, B)