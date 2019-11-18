# Matrix Multiplication Method Comparison

### This project is a multiprocessing implementation of Matrix Multiplication


## How to start

1. Generate matrix data by executing matrix_generation script

```
    python notebook/matrix_generation.py
```
After running the script, a test_data directory is generated with matrix data.

2. To run all the script together, execute main.py by
```
    python main.py
```

3. To run the algorithms indivisually with arguements, executes
```
    python 1_vanilla.py -s 2
```
or
```
    python 2_vanilla_parallel.py -s 2 -t 2
```
or
```
    python 3_strassen.py -s 2
```

Notes: 

1. `-s` refers to size of the matrix, which can only be the power of 2
2. `-t` refers to the number of thread, which can only be the power of 2 and equal or smaller than the matrix size.


## How to read result

After executing the script, i.e. `main.py`, a list of results is to be printed. It can be interpreted as follows:

```
Parallel Matrix Multiplication    <---- algorithm name
Matrix Size: 2                    <---- matrix size
Thread Number: 2                  <---- thread number (only for parallel algo)


real    0m0.411s                  <---- clock time
user    0m0.170s                  <---- user time
sys     0m0.075s                  <---- system time
```

[More info about time:](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1)

One of these things is not like the other. Real refers to actual elapsed time; User and Sys refer to CPU time used only by the process.

Real is wall clock time - time from start to finish of the call. This is all elapsed time including time slices used by other processes and time the process spends blocked (for example if it is waiting for I/O to complete).

User is the amount of CPU time spent in user-mode code (outside the kernel) within the process. This is only actual CPU time used in executing the process. Other processes and time the process spends blocked do not count towards this figure.

Sys is the amount of CPU time spent in the kernel within the process. This means executing CPU time spent in system calls within the kernel, as opposed to library code, which is still running in user-space. Like 'user', this is only CPU time used by the process. See below for a brief description of kernel mode (also known as 'supervisor' mode) and the system call mechanism.

User+Sys will tell you how much actual CPU time your process used. Note that this is across all CPUs, so if the process has multiple threads (and this process is running on a computer with more than one processor) it could potentially exceed the wall clock time reported by Real (which usually occurs). Note that in the output these figures include the User and Sys time of all child processes (and their descendants) as well when they could have been collected, e.g. by wait(2) or waitpid(2), although the underlying system calls return the statistics for the process and its children separately.