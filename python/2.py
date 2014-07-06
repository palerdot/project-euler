x = 0
y = 1

limit = 4*(10**6)
print limit

s = x+y
total = 0

while s < limit:
    if s%2 == 0:
        total += s

    x = y
    y = s

    s = x+y

print 'sum is %d' % total
