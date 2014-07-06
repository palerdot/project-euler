x = 3
y = 5
target = 1000

total = []

multiple = 0
product = x

for product in range(x, target):
    
    multiple += 1
    product = x*multiple
    
    if product < target:
        # get all the multiples of x
        total.append(product)

multiple = 0
product = y

for product in range(y, target):
   
    multiple += 1
    product = y*multiple
    
    if (product % x)  == 0:
        # we have already counted in the previous loop
        continue
    elif product < target:
        # get all the multiples of y, excluding the multiples of x
        total.append(product)

#print total
print sum(total)
