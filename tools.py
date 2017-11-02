#!/usr/bin/env python
from math import sqrt


def is_prime(n):  
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def get_prime_list(start, end):
    prime_list = list()
    for i in range(start, end + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def get_prime_factor(n):
    num = n
    prime_factor_list = list()
    i = 2
    while i <= num:  
        if is_prime(i) and num % i == 0:  
            num /= i  
            prime_factor_list.append(i)  
        i += 1
    return prime_factor_list


if __name__ == '__main__':
    #print get_prime_list(1, 10000)
    print get_prime_factor(600851475143)

