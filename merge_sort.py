#!/usr/bin/env python3

import numpy as np


# takes two arrays of the same size
# outputs the sorted array
def merge(a, b):
    output = []
    for a, b in zip(a, b):
        if a > b:
            output.append(b)
            output.append(a)
            continue
        output.append(a)
        output.append(b)

    return output

def merge_sort(array):
    # split arrays
    arrayA = array[:int(len(array)/2)]
    arrayB = array[int(len(array)/2):]

    if len(arrayA) <= 1 or len(arrayB) <= 1:
        return merge(arrayA, arrayB)

    return merge_sort(arrayA), merge_sort(arrayB)


def main(n):
    arrayA = np.random.randint(0,9,n)
    print(arrayA)
    print(merge_sort(arrayA))
    

if __name__ == '__main__':
    main(10)

