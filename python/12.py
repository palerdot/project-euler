import time
import math
import itertools

start_time = time.time()

# keeps track of the index of current triangle number
CURRENT_INDEX = 1
# keeps track of the number itself
CURRENT_TRIANGLE_NUMBER = 1

DIVISORS_THRESHOLD = 500

def find_factors(n):
    limit = int(math.floor(math.sqrt(n))) + 1
    
    # the list that contains list of factors
    # for example, for 6 it will contain
    # [[1, 6], [2, 3]]
    factors = []
    for x in range(1, limit):
        if n%x == 0:
            # we have encountered a pair of factors
            # save it
            if (n/x) != x:
                factors.append([n/x, x])

    return factors


def increment_triangle_number():
	global CURRENT_INDEX
	global CURRENT_TRIANGLE_NUMBER

	# increment index by 1
	CURRENT_INDEX = CURRENT_INDEX + 1

	# calculate the triangle number
	CURRENT_TRIANGLE_NUMBER = (CURRENT_INDEX * (CURRENT_INDEX + 1)) / 2

	# return the current triangle number
	return CURRENT_TRIANGLE_NUMBER

def triangle_number_check():

	# gets the factor pairs
	factor_pairs = find_factors(CURRENT_TRIANGLE_NUMBER)
	# gets the final list of all the factors of the number
	factors_list = list(itertools.chain(*factor_pairs))

	return len(factors_list) < DIVISORS_THRESHOLD

# while the divisors of current triangle number is less than our threshhold
while (triangle_number_check()):
	# find the next triangle number
	increment_triangle_number()

# we now should have our required triangle number
print CURRENT_TRIANGLE_NUMBER, " IS OUR TRIANGLE NUMBER"


print time.time() - start_time, "seconds"