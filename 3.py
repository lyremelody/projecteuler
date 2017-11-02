#!/usr/bin/env python


from tools import get_prime_factor


def get_max_prime_factor(n):
    return get_prime_factor(n)[-1]


if __name__ == '__main__': 
    print get_max_prime_factor(600851475143)
