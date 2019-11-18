# %%
import numpy as np
import os
from numpy import genfromtxt

# %%
base_path='./test_data'

# %%
if not os.path.exists(base_path):
    os.makedirs(base_path)

# %%
sizes = [2, 4,8,16,32,64,128,256, 512,1024]

# %%
for size in sizes:
    A = np.random.randint(100,999,(size,size))
    B = np.random.randint(100,999,(size,size))
    file_A = 'A_' + str(size) + '.csv'
    file_B = 'B_' + str(size) + '.csv'
    path_A = os.path.join(base_path, file_A)
    path_B = os.path.join(base_path, file_B)
    print(path_A)
    print(path_B)
    np.savetxt(path_A, A, fmt='%i',delimiter=",")
    np.savetxt(path_B, B, fmt='%i',delimiter=",")

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
    print(A.shape)
    print(B.shape)

# %%
