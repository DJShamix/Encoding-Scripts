
from tkinter import N


def bin_2_gray(n):

    n = int(n, 2)
    n ^= (n >> 1)

    return bin(n)[2:]


def gray_2_bin(n):

    n = int(n, 2)

    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask

    return bin(n)[2:]


def test_bin_2_gray():
    g = input('Enter bin number: ')
    b = bin_2_gray(g)
    print('Bin {} number in Gray is: {}\n'.format(g, b))

def test_gray_2_bin():
    g = input('Enter gray number: ')
    b = gray_2_bin(g)
    print('Gray {} number in Bin is: {}\n'.format(g, b))



test_bin_2_gray()
test_gray_2_bin()