import time

start_time = time.time()

def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n-1)

def sum_of_digits(num):
    TOTAL = 0

    while (num > 0):
        QUOTIENT = num/10
        REMAINDER = num%10

        TOTAL = TOTAL + REMAINDER

        num = num/10

    return TOTAL

factorial = fact(100)

print "sum => ", sum_of_digits(factorial) 

print time.time() - start_time, " seconds"