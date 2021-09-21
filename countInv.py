#!/usr/bin/env python3

def read_data_file(file_name):
    with open(file_name, 'r',) as f:
        return [int(line.strip()) for line in f.readlines()]

def merge_count_split_inv(C, D):
    B = []
    i = j = invs = 0

    while i < len(C) and j < len(D):
        if C[i] <= D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            j += 1
            invs += len(C) - i

    while i < len(C):
        B.append(C[i])
        i += 1

    while j < len(D):
        B.append(D[j])
        j += 1

    return invs, B


def count_inv(A):
    n = len(A)
    m = n//2

    if n == 0 or n == 1:
        return 0, A

    C = A[:m]
    D = A[m:]

    left_inv, C_sorted = count_inv(C)
    right_inv, D_sorted = count_inv(D)
    split_inv, B = merge_count_split_inv(C_sorted,D_sorted)

    return (left_inv + right_inv + split_inv), B

def main(file_name):
    data_array = read_data_file(file_name)
    print(count_inv(data_array)[0], f'inversions, {len(data_array)} elements')

if __name__ == '__main__':
    main('./problem3.5.txt')
    main('./problem3.5test.txt')

