import time 
import math

start_time = time.time()

AMICABLES = []

# for a given number returns a list containing all its divisors (excluding itself)
def get_divisors(num):
    # by default add 1
    divisors = [1]

    # all one-half of divisors will fall within the range of sqrt(num);
    LIMIT = int(math.ceil( math.sqrt(num) ))

    for n in range(2, LIMIT):
        if (num%n == 0):
            # this number divides our number
            divisors.append(n)
            divisors.append(num/n)

    return divisors


# determines if a given number has an amicable pair
# if yes adds to our amicable list
def find_amicable(num):

    global AMICABLES

    # do not proceed if we have already found an amicable pair for this number
    if num in AMICABLES:
        return

    divisors = get_divisors(num)
    amicable_pair = sum(divisors)
    # find the sum of divisors for amicable pair
    amicable_divisors_sum = sum( get_divisors(amicable_pair) )

    if (num == amicable_divisors_sum):
        # we got an amicable pair; (amicable pairs are only if the two numbers are different)
        if (num != amicable_pair):
            AMICABLES.append(num)
            AMICABLES.append(amicable_pair)

# let us calculate all the amicable pairs
for x in range(1, 10000):
    find_amicable(x)

print "sum of amicables ", sum(AMICABLES), AMICABLES

print time.time() - start_time, " seconds"