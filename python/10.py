import math
import time

start_time = time.time()

def sum_of_primes():

    # start looking for primes from 2 
    start = 2

    # start with an initial sum of 0 
    total = 0

    # limit till which primes has to be generated
    prime_max = 2*(10**6)

    for p in range(2, prime_max):
        if is_prime(p):
            # we have got a prime number
            # add this to sum
            total += p
            
    print total,": Total of primes till", prime_max
        

def is_prime(num):
    """
    calculates if a number is prime or not in the
    order of O(log n) => here for a number n, all the 
    numbers from 2 to n^1/2 is checked for divisibility.
    n^1/2 = 1/2*log(n) = O(log n).

    A small comparision;

    range(2, n-1) => O(n) [normal test for divisibility]
    range(2, n/2) => O(n) [factors can be atmost in this range]
    range(2, n^1/2) => O(log n) [factors repeat by interchanging after this
    range]
    """

    if num == 2:
        return True

    limit = int(math.ceil(math.sqrt(num))) + 1

    for n in range(2, limit):
        if num%n == 0:
            return False 
        
    return True

sum_of_primes()

print time.time() - start_time, "seconds"
