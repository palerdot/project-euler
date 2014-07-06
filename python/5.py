import time
import math

start_time = time.time()

def factorize_into_primes(num):
    # lists that hold the factors of the given num
    factors = []

    start = int(math.ceil(math.sqrt(num)))
    end = 0
    step = -1

    for x in xrange(start, end, step):
        # if the number is divisible
        if num%x == 0:
            # we have got a set of factors, the product
            # of which gives the num; break into prime
            if is_prime(x):
                factors.append(x)
            else:
                first = factorize_into_primes(x)
                factors.extend(first)

            if is_prime(num/x):
                factors.append(num/x)
            else:
                second = factorize_into_primes(num/x)
                factors.extend(second)
            
            # we got a set of factors; don't proceed
            # further
            break

    return factors
    
            
# ----------------------------------------------------

def is_prime(num):
    """
        checks if a number is prime;
        checks for divisibility of a number num
        from n/2 to 2; if it is not divisible
        it is a prime
    """

    if num < 3:
        return True

    # check if the number is divisible in the range of
    # sqrt(num), 2; after the square root the factors
    # flips themselves

    # square root of the number is the upper limit 
    upper_limit = int(math.ceil(math.sqrt(num)))
    
    for x in xrange(upper_limit, 1, -1):
       
        if (num%x) == 0:
            return False

    return True


# ----------------------------------------------------

#x = raw_input("Enter a number: ")
#print factorize_into_primes(int(x))

limit = 20  

primes = []
composites = []

factor_list = []

for x in xrange(2, limit+1, 1):
    if is_prime(x):
        primes.append(x)
    else:
        composites.append(x)

for c in composites:
    # get the factors of this composite number
    factor_list = factorize_into_primes(c)

    # convert the list of prime factors into
    # a set of distinct elements
    distinct_factors = set(factor_list)

    # for each distinct element, get the count in
    # the factor list; if the count is greater than 1,
    # add the exceess count to the prime list

    for distinct in distinct_factors:
        count = factor_list.count(distinct) - primes.count(distinct)
        
        # python does not consider 0 as False !, so ....
        while count > 0:
            primes.append(distinct)
            count -= 1

from operator import mul
print reduce(mul, primes, 1)
        
print time.time() - start_time, "seconds"    



