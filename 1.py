#!/usr/bin/env python


def sum_of_multiples(base, max_limit):
    max_multiple = (max_limit - 1)/base
    sum_multiple = 0

    for i in xrange(max_multiple + 1):
        sum_multiple += i 

    return base * sum_multiple


def my_first_solution():
    result = sum_of_multiples(3, 1000) + sum_of_multiples(5, 1000) - sum_of_multiples(3 * 5, 1000)
    return result


# via YiannisAyianis
def other_ways():
    return sum(x for x in range(1000) if x%3==0 or x%5==0)


if __name__ == '__main__':
    print my_first_solution()
    print other_ways()
    
