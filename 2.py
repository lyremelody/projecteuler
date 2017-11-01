#!/usr/bin/env python


def sum_of_fibonacci_even(max_limit):
    a = 1
    b = 2
    c = a + b

    sum_of_even = b
    while c < max_limit:
        a = b
        b = c
        c = a + b
        if c > max_limit:
            break

        print c 
        if c % 2 == 0:
            sum_of_even += c
 
    return sum_of_even

if __name__ == '__main__':
    result = sum_of_fibonacci_even(4000000)
    print 'result: ', result
        
