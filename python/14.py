# -*- coding: utf-8 -*-

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# TODO: Is there any better mathematical way of doing this ?

import time
import math

start_time = time.time()

CURRENT = 1

START = 1
# maximum till which we have to calculate the collatz sequence
MAXIMUM = 1000000

COLLATZ_SEQUENCE = []

# contains the current max sequence length
MAX_SEQUENCE_LENGTH = 1

# contains for which value maximum value is found
MAX_FOR = 1

# rule for even numbers
def even_rule(n):
    return n/2

# rule for odd numbers
def odd_rule(n):
    return 3*n + 1

# returns true if the given number is odd; false if even
def is_even(n):
    return n%2 == 0

# takes a number and returns the next number in the collatz sequence
def calc_next_collatz_number(n):
    
    global CURRENT
    global COLLATZ_SEQUENCE

    # calculate the next number
    if (is_even(n)):
        next = even_rule(n)
    else:
        next = odd_rule(n)

    # append the number to sequence
    COLLATZ_SEQUENCE.append(next)
    # update the current collatz number
    CURRENT = next

# calculates the collatz sequence for a number
def calc_collatz_sequence(n):
    
    global COLLATZ_SEQUENCE
    global CURRENT

    COLLATZ_SEQUENCE = []

    CURRENT = n
    COLLATZ_SEQUENCE.append(CURRENT)
    
    while (CURRENT != 1):
        calc_next_collatz_number(CURRENT)


# calculate collatz sequence for our range
for i in range(START, MAXIMUM):

    # calculate the sequence for this number
    calc_collatz_sequence(i)

    # update the max value
    if (len(COLLATZ_SEQUENCE) > MAX_SEQUENCE_LENGTH):
        MAX_SEQUENCE_LENGTH = len(COLLATZ_SEQUENCE)
        MAX_FOR = i

print "max for ", MAX_FOR, " LENGTH: ", MAX_SEQUENCE_LENGTH
    

print time.time() - start_time, " seconds"