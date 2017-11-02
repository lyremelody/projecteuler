#!/usr/bin/env python

from tools import is_palindromic


def get_max_palindromic(digit):
    start = 10 ** (digit - 1)
    end = 10 ** digit - 1
    num = 0
    for i in range(start, end):
        for j in range(start, end):
            n = i * j
            if is_palindromic(n) and n > num:
                num = n
    return num


if __name__ == '__main__': 
    print get_max_palindromic(1)
    print get_max_palindromic(2)
    print get_max_palindromic(3)
