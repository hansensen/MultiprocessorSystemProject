from optparse import OptionParser
from math import ceil, log
from time import process_time
import numpy as np
import os
from numpy import genfromtxt
from optparse import OptionParser

print('Strassen Algorithm')

def vanilla_matrix_mul(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add_mul(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract_mul(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassenR(A, B):
    n = len(A)

    # stop conditon for recursive strassen algo
    if n < int(stop_condition):
        return vanilla_matrix_mul(A, B)
    else:
        # initializing the new sub-matrices
        new_size = int(n/2)
        a11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        b11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        aResult = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        bResult = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        # dividing the matrices in 4 sub-matrices:
        for i in range(0, new_size):
            for j in range(0, new_size):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + new_size]    # top right
                a21[i][j] = A[i + new_size][j]    # bottom left
                a22[i][j] = A[i + new_size][j + new_size] # bottom right

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + new_size]    # top right
                b21[i][j] = B[i + new_size][j]    # bottom left
                b22[i][j] = B[i + new_size][j + new_size] # bottom right

        # Calculating p1 to p7:
        aResult = add_mul(a11, a22)
        bResult = add_mul(b11, b22)
        p1 = strassenR(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

        aResult = add_mul(a21, a22)      # a21 + a22
        p2 = strassenR(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = subtract_mul(b12, b22) # b12 - b22
        p3 = strassenR(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = subtract_mul(b21, b11) # b21 - b11
        p4 =strassenR(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = add_mul(a11, a12)      # a11 + a12
        p5 = strassenR(aResult, b22)  # p5 = (a11+a12) * (b22)

        aResult = subtract_mul(a21, a11) # a21 - a11
        bResult = add_mul(b11, b12)      # b11 + b12
        p6 = strassenR(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

        aResult = subtract_mul(a12, a22) # a12 - a22
        bResult = add_mul(b21, b22)      # b21 + b22
        p7 = strassenR(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add_mul(p3, p5) # c12 = p3 + p5
        c21 = add_mul(p2, p4)  # c21 = p2 + p4

        aResult = add_mul(p1, p4) # p1 + p4
        bResult = add_mul(aResult, p7) # p1 + p4 + p7
        c11 = subtract_mul(bResult, p5) # c11 = p1 + p4 - p5 + p7

        aResult = add_mul(p1, p3) # p1 + p3
        bResult = add_mul(aResult, p6) # p1 + p3 + p6
        c22 = subtract_mul(bResult, p2) # c22 = p1 + p3 - p2 + p6

        # concat two matrix to get a new matrix
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, new_size):
            for j in range(0, new_size):
                C[i][j] = c11[i][j]
                C[i][j + new_size] = c12[i][j]
                C[i + new_size][j] = c21[i][j]
                C[i + new_size][j + new_size] = c22[i][j]
        return C

def get_next_power_of_two(n):
    power_of_two = 2**int(ceil(log(n,2)))
    return power_of_two

def strassen(A, B):
    n = len(A)
    m = get_next_power_of_two(n)
    # create new A and B matrix with size ms
    A_new = np.zeros((m,m),dtype=int)
    B_new = np.zeros((m,m),dtype=int)
    for i in range(n):
        for j in range(n):
            A_new[i][j] = A[i][j]
            B_new[i][j] = B[i][j]
    C_new = strassenR(A_new, B_new)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = C_new[i][j]
    return C

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
    (options, args) = parser.parse_args()

    print('Matrix Size: {}'.format(options.size))
    size = options.size

    file_A = 'A_' + str(size) + '.csv'
    file_B = 'B_' + str(size) + '.csv'
    path_A = os.path.join(base_path, file_A)
    path_B = os.path.join(base_path, file_B)

    A = genfromtxt(path_A, delimiter=',')
    B = genfromtxt(path_B, delimiter=',')
    num_thread = 2

    n, m,l= len(A), len(A[0]), len(B[0])

    C = np.zeros((n, l))
    print(C.shape)
    # according to the num_thread, divide matrix A into parts
    part = int(len(A) / num_thread)
    if part < 1:
        part = 1

    stop_condition = 2
    C = strassen(A, B)