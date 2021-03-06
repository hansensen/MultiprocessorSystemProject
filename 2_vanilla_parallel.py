# %%
import numpy as np
import multiprocessing
import os
from numpy import genfromtxt
from optparse import OptionParser
import math

print('Parallel Matrix Multiplication')

# %%
def lineMult(start):
    global A, B, C, part
    n = len(A)
    # print('starts from {} and ends {}'.format(start, start+part))
    for i in range(start, start+part):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# %%
def ikjMatrixProduct(A, B, num_thread):
    n = len(A)
    pool = multiprocessing.Pool(num_thread)
    # print(list(range(0, n, part)))
    results = pool.map(lineMult, list(range(0,n, part)))
    return sum(results)

# %%
base_path='./test_data'


# %%
if __name__ == "__main__":
    parser = OptionParser()
    # takes size as an arg
    parser.add_option("-s",
                      dest="size",
                      default="2",
                      help="input matrix size")

    parser.add_option("-t",
                    dest="thread",
                    default="1",
                    help="input thread number")
    (options, args) = parser.parse_args()

    print('Matrix Size: {}'.format(options.size))
    print('Thread Number: {}'.format(options.thread))

    size = options.size
    num_thread = int(options.thread)

    file_A = 'A_' + str(size) + '.csv'
    file_B = 'B_' + str(size) + '.csv'
    path_A = os.path.join(base_path, file_A)
    path_B = os.path.join(base_path, file_B)

    A = genfromtxt(path_A, delimiter=',')
    B = genfromtxt(path_B, delimiter=',')
    
    n, m,l= len(A), len(A[0]), len(B[0])
    C = np.zeros((n, l))
    part = int(len(A) / num_thread)
    if part < 1:
        part = 1
    C = ikjMatrixProduct(A, B, num_thread)

    print()