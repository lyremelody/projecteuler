#!/usr/bin/env python


def sum_of_multiples(base, max_limit):
    max_multiple = (max_limit - 1)/base
    sum_multiple = 0

    for i in xrange(max_multiple + 1):
        sum_multiple += i 

    return base * sum_multiple


if __name__ == '__main__':
    print sum_of_multiples(3, 10)
    print sum_of_multiples(5, 10)
    print sum_of_multiples(3, 1000)
    print sum_of_multiples(5, 1000)

    result = sum_of_multiples(3, 1000) + sum_of_multiples(5, 1000) - sum_of_multiples(3 * 5, 1000)
    print "solution is: ", result

