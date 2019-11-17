from optparse import OptionParser
import os

if __name__ == "__main__":
    parser = OptionParser()
    # sizes = [2, 100, 1000, 2000, 5000, 10000]
    sizes = [2, 100]

    for size in sizes:
        print('matrix size: {}'.format(size))

        os.system('time python ./1_vanilla.py -s {}'.format(size))
        os.system('time python ./2_vanilla_parallel.py -s {}'.format(size))
        os.system('time python ./3_strassen.py -s {}'.format(size))