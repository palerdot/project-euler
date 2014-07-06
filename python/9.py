import math
import time

start_time = time.time()

def fibonacci_method():
    """
    This module uses the method devised by the great 
    'Fibonacci - Leonardo of Pisa' to generate pythagorean
    triplets.

    Basic idea: a^2 - b^2 = (a+b)(a-b) = c^2
    Difference of two consecutive integers a,b will result in
    a^2 - b^2 = (a+b) which should be a square number.

    Sum of two consecutive numbers will be an odd number. Only
    square of odd numbers is an odd number.

    Look for each odd number, for example - 3. 3^2 = 9.
    Now, when we write the odd numbers in a sequence like 
    1, 3, 5, 7, 9, ..... The position of 9 is 5; so the two numbers
    'a' and 'b' are 5(a), and 4(b = a-1).
    """

    #start with a dummy total of 0
    total = 0

    # start with odd number 3; 
    num = 3

    while total <= 1000:
        # calculate the square
        square = num**2 

        # find the position of the square
        a = (square+1)/2
        b = a-1

        # we are following the convention a^2 = b^2 + c^2
        c = int(math.sqrt(a**2 - b**2))

        # save the total of the triplet
        total = a+b+c

        # go to next odd number
        num += 2

        if total == 1000:
            display_special_triplets(a,b,c,'Fibonacci')
            return True

    return False
    

def euclid_method():
    """
    This method deals primarily with even numbers
    for any even number 2n = 2ab, find the factor pairs
    of ab. for example 6 = 2*3; factor pairs are (3, 1)
    then 3^2 - 1^2, 6(the number itself), 3^2 + 1^2
    are the pythagorean triplets

    This kind of triplets occurs for every factor pairs
    """

    # start with even number 4
    num = 4

    # start with a dummy total of 0
    total = 0

    #target sum is the variable which holds the sum of the
    # required triplets
    target_sum = 1000

    while True:
        n = num/2
        # find the factors of n
        # it will return a list of list where each
        # individual list contains two factors that make
        # up 'n'
        
        n_factors = find_factors(n)

        for factors in n_factors:
            # incoming factors is list containing a pair of
            # factors whose product make up n

            # factors[1] = x, factors[0] = y
            # the triplets would be
            # x^2 - y^2, num, x^2 + y^2
            
            x = factors[0]
            y = factors[1]

            a = x**2 - y**2
            b = num
            c = x**2 + y**2

            total = a+b+c
            
            if total == target_sum:
                display_special_triplets(a, b, c, 'Euclid')
                return
            print total

        # increment to next even number
        num += 2
            
    print "[not found] special triplets not found in 'Euclid Method'"
        

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


def display_special_triplets(a, b, c, method = 'Fibonacci'):
    
    print "************************************************"
    print "Found Special Triplets using '%s' method" % method
    print "************************************************"

    # we got the special pythagorean triplet
    # with the sum of 1000
    a = int(a)
    b = int(b)
    c = int(c)

    print "a - %d" % a
    print "b - %d" % b
    print "c - %d" % c
    total = a+b+c
    print "sum - ", a+b+c
    print "************************"
    product = a*b*c
    print "product - %d" % product
    print "************************"
    print "Thanks to ", method
    print "************************" 
    return


def find_special_pythagorean_triplet():
    fibonacci_method()
    euclid_method()

find_special_pythagorean_triplet()

print time.time() - start_time, "seconds"
