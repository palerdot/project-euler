# Problem 16

# not sure if there is a Math trick; trying it in a conventional way

import time
import math

start_time = time.time()

our_num = str(pow(2, 1000))

print "num is ", our_num

length = len(our_num)

# will contain the final sum
THE_SUM = 0

for i in range(0, length):
	THE_SUM = THE_SUM + int( our_num[length - i - 1] )

print "sum is ", THE_SUM

print time.time() - start_time, " seconds"