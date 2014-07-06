import math
import time

start_time = time.time()

# constructing the given string

s = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

test_number = ()

for digit in s:
    test_number += (digit, )

# limit for consecutive number of products to be found out
limit = 13

# following dictionary contains 3 values for max product calculation
# value, start_index, end_index

# consider first 13 as the initial set of values

maximum = {'product': 1, 'start_index': 0, 'end_index': limit}

start = maximum['start_index']
end = maximum['end_index']

# initial population of values; considering the product of 
# first 13 as starting values; constructing a list which will
# hold the sample set of 13 values as we proceed
sample_list = []
product = 1

for x in range(start, end):
    product *= int(test_number[x])
    sample_list.append(int(test_number[x]))

maximum['product'] = product

while end < len(test_number): 
        
    num = int(test_number[end])

    if num != 0:
        # if the incoming number is not zero
        first = sample_list.pop(0)
        sample_list.append(num)

        
        # don't waste time multiplying all values again; 
        if first != 0:
            product = (product/first)*num
        else:
            # the first value is zero; no other option
            product = reduce( lambda x,y: x*y, sample_list)    

        if product == 0:
            # there is a zero in the list; move indexes to 
            # exclude the zero
            zero_idx = sample_list.index(0)
            start = start + zero_idx + 1
            end = end + zero_idx + 1
        else:
            if product > maximum['product']:
                maximum['product'] = product

            start += 1
            end += 1
    else:
        # the incoming number is 0; no point in wasting time
        # multiplying the numbers with this zero; shift indexes
        
        # shifting the consecutive zeroes if any
        while num != 0:
            start += 1
            end += 1
            num = int(test_number[end])

        start = end + 1
        end = start + limit
        
        if end > len(test_number):
            end = len(test_number)

        # reconstruct the sample list; # give a dummy initial 
        # value to prevent reduce
        sample_list = []
        for digit in range(start, end):
            sample_list.append(int(test_number[digit]))

        if len(sample_list) > 0:   
            product = reduce(lambda x, y: x*y, sample_list)

        if product > maximum['product']:
            maximum['product'] = product


print maximum['product'], "is the maximum product"

print time.time() - start_time, "seconds"


