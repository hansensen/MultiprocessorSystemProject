# %%
import numpy as np
import multiprocessing
import os
from numpy import genfromtxt
from optparse import OptionParser

print('Parallel Matrix Multiplication')

# %%
def lineMult(start):
    global A, B, C, part
    n = len(A)
    print('starts from {} and ends {}'.format(start, start+part))
    for i in range(start, start+part):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# %%
def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    pool = multiprocessing.Pool(threadNumber)
    print(list(range(0, n, part)))
    results = pool.map(lineMult, list(range(0,n, part)))
    return sum(results)

# %%
base_path='./test_data'

# %%
if not os.path.exists(base_path):
    os.makedirs(base_path)

# %%
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s",
                      dest="size",
                      default="2",
                      help="input matrix size")
    (options, args) = parser.parse_args()

    print(options.size)
    size = options.size

    file_A = 'A_' + str(size) + '.csv'
    file_B = 'B_' + str(size) + '.csv'
    path_A = os.path.join(base_path, file_A)
    path_B = os.path.join(base_path, file_B)
    print('input data:')
    print(path_A)
    print(path_B)
    A = genfromtxt(path_A, delimiter=',')
    B = genfromtxt(path_B, delimiter=',')
    threadNumber = 2
    n, m, p = len(A), len(A[0]), len(B[0])
    C = np.zeros((n, p))
    print(C.shape)
    part = int(len(A) / threadNumber)
    if part < 1:
        part = 1
    C = ikjMatrixProduct(A, B, threadNumber)