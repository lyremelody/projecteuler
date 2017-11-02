#!/usr/bin/env python


# solution 1
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


# solution 2
def fibonacci_sequence(max_limit):
    fib_seq = list([1, 2])
    while True:
        tmp = fib_seq[-1] + fib_seq[-2]
        if tmp > max_limit:
            break
        fib_seq.append(tmp)
    return fib_seq


def sum_of_fibonacci_even2(max_limit):
    sum_of_even = 0
    for el in fibonacci_sequence(max_limit):
        if el % 2 == 0:
            sum_of_even += el

    return sum_of_even


if __name__ == '__main__':
    #result = sum_of_fibonacci_even(4000000)
    #print 'result: ', result

    result = sum_of_fibonacci_even2(4000000)
    print 'result: ', result
        
