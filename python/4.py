import math
import time

start_time = time.time()

def is_palindrome(num):
    num_list = [int(i) for i in str(num)]
    num_length = len(num_list)

    #print num_length/2
    is_palindrome = True
    
    for x in range(0, num_length/2):
        start = num_list[x]
        end = num_list[num_length - x - 1]
        if start != end:
            is_palindrome = False
            break

    return is_palindrome

def is_n_digit_num( digit, number ):
    """
        finds out if a number contains n digit
        for ex: is_n_digit_number(2, 10) => True
    """
    total_digits = 0

    while number:
        total_digits += 1
        number = number/10
        if total_digits > digit:
            return False

    if total_digits == digit:
        return True
    else:
        return False

def find_total_digits(number):
    """
        finds out total digits in a number
    """
    total_digits = 0

    while number:
        total_digits += 1
        number = number/10
        
    return total_digits 

def find_largest_palindrome():
    start = 999 * 999
    end = 100 * 100

    for i in range( start, end - 1, -1  ):
        if is_palindrome(i):
            # we have a palindrome; check the factors
            # and see if it is a product of two digit numbers
            p_start = int( math.ceil( math.sqrt(i) ) )
            p_end = 9

            digit = 3

            for x in range(p_start, p_end, -1):
                if i%x == 0:
                    # this is a factor; check for digits
                    # of this factor and its product
                    if is_n_digit_num(digit, x) and is_n_digit_num(digit, i/x):
                        # we got the largest palindrome digit
                        return i

                    # check if total digits of incoming factor is
                    # less than 3; in that case no need to proceed
                    if find_total_digits(x) > digit:
                        continue
                    elif find_total_digits(x) < digit:
                        break
        else:
            continue

print find_largest_palindrome()
print time.time() - start_time , "seconds"



