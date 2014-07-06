import math
import time

start_time = time.time()

def find_largest_prime_factor(num):
    """
    finds out largest prime factor for a number n, 
    There factors are in two ranges repeating themselves
    
    upper range => range(sqrt(num), num)
    lower range => range(2, sqrt(num))

    lower range is lesser in number; start with it;
    if a number is divisible in lower range, check if the 
    quotient in the upper range is prime;

    if no number in upper range is a prime, go for the lower
    range numbers

    """
    # square root of the number is the upper limit
    upper_limit = int(math.ceil(math.sqrt(num)))  

    # consists of lower half of divisors in range(sqrt(num), 2)
    lower_half = []

    start = 2
    end = upper_limit + 1
    step = 1

    for x in xrange(start, end, step):
        
        # check if the number is divisible;
        # if it is divisible; check if the quotient
        # is prime;
        if num%x == 0:
            # checks for prime factors in range(num-1, sqrt(num))
            if is_prime(num/x): 
                # found the largest prime factor
                return num/x
            else:
                # save it for later calculations to find
                # highest prime in lower range (sqrt(num), 2)
                lower_half.insert(0, x) 

    # there is no prime in the upper half;
    # try in the lower half
    # the list will be in descending order

    for y in lower_half:
        if is_prime(y):
            return y

    # the given number itself is a prime
    return num

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
    upper_limit = int(math.ceil(math.sqrt(num))) + 1
    
    for x in xrange(2, upper_limit, 1):
       
        if (num%x) == 0:
            return False

    return True


# ----------------------------------------------------


number = 600851475143

print find_largest_prime_factor(number)
print time.time() - start_time, "seconds"

