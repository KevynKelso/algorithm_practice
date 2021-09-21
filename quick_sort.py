import math
import time

import numpy as np
import matplotlib.pyplot as plt


def read_data_file(file_name):
    with open(file_name, 'r',) as f:
        return [int(line.strip()) for line in f.readlines()]

def plot_vs_nlogn(times, ns):
    plt.plot(ns, times, label='Actual')
    plt.plot(ns, np.array([ x*math.log(x,2) for x in ns ])/10000000, label='Theoretical (nlogn)')
    plt.title('Actual Running Time of Quicksort vs Theoretical')
    plt.ylabel('Time (seconds)')
    plt.xlabel('n (number of elements)')
    plt.legend()
    plt.show()

# ----------------- Quick Sort Code ---------------------------------------
def partition(A, l, r):
    p = A[l]
    pointer = l + 1

    for i in range(l+1,r+1):
        if A[i] < p:
            tmp = A[i]
            A[i] = A[pointer]
            A[pointer] = tmp
            pointer += 1

    tmp = A[l]
    A[l] = A[pointer-1]
    A[pointer-1] = tmp

    return pointer-1

def quick_sort(A, l, r):
    if l >= r:
        return A

    j = partition(A,l,r)
    quick_sort(A,l,j-1)
    quick_sort(A,j+1,r)
# ----------------- END Quick Sort Code ---------------------------------------

def main(filenames):
    times = []
    ns = []

    for filename in filenames:
        array = read_data_file(filename)

        start = time.time()
        quick_sort(array, 0, len(array)-1)
        end = time.time()

        print(array)
        print(f'Took: {end - start}')

        times.append(end - start)
        ns.append(len(array))

        print(f'\nTimes: {times}\nN\'s: {ns}')

    plot_vs_nlogn(times, ns)


if __name__ == '__main__':
    filenames = "./data/problem5.6test1.txt ./data/problem5.6test2.txt ./data/problem5.6test3.txt".split(' ')
    main(filenames)

