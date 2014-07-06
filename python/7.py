# to generate 10001 th prime

import math
import time

start_time = time.time()

def generate_primes(prime_index):
    # start with 2; this is the list that is going to 
    # contain the list of generated primes
    primes = [2]

    # start looking for primes from 3
    start = 3

    while len(primes) < (prime_index):

        # use this method to find out if a
        # number is prime by checking if the number has
        # any prime factors from the current list of primes
        # using method, also reduces the confusion of having
        # nested loops to break out of;

        if is_prime(start):
            primes.append(start)

        start += 1
        
    # the while loop has stopped; the last prime is our 
    # desired value
    prime = primes.pop()
    return prime

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

p_index = 10001

p = generate_primes(p_index)
print p, "is the %dth prime" % p_index

print time.time() - start_time, "seconds"
