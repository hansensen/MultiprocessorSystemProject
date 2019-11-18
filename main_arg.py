from optparse import OptionParser
import os

if __name__ == "__main__":
    parser = OptionParser()
    # sizes = [2, 100, 1000, 2000, 5000, 10000]
    sizes = [2, 128, 512, 1024, 2048]

    for size in sizes:
        print('matrix size: {}'.format(size))

        os.system('time python ./1_vanilla.py -s {}'.format(size))
        os.system('time python ./3_strassen.py -s {}'.format(size))

    os.system('time python ./2_vanilla_parallel.py -s {} -t {}'.format(2, 2))

    threads = [2,4,8,16,32,64,128]
    for thread in threads:
        os.system('time python ./2_vanilla_parallel.py -s {} -t {}'.format(128, thread))


    threads = [2,4,8,16,32,64,128,256,512]
    for thread in threads:
        os.system('time python ./2_vanilla_parallel.py -s {} -t {}'.format(512, thread))

    threads = [2,4,8,16,32,64,128,256,512,1024]
    for thread in threads:
        os.system('time python ./2_vanilla_parallel.py -s {} -t {}'.format(1024, thread))

    threads = [2,4,8,16,32,64,128,256,512,1024,2048]
    for thread in threads:
        os.system('time python ./2_vanilla_parallel.py -s {} -t {}'.format(2048, thread))
