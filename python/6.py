import math
import time 

start_time = time.time()

# to find the difference of 
# (a + b + ... )^2 - (a^2 + b^2 + .....)
# by applying formula the result will be
# 2*(ab + bc....)

limit = 100
nsum = 0


for num in range (1, limit+1, 1):
    s = 0
    for x in range(num+1, limit+1, 1):
        s += x
    temp_sum = num*s
    nsum += temp_sum

print 2*nsum

print time.time() - start_time, "seconds"



