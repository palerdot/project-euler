# Note: solved using dynamic programming by splitting the list into small triangles from bottom
# reference: http://www.mathblog.dk/project-euler-18/

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

import time
import math

start_time = time.time()

ORIGINAL_DATA = []

# reads a file and returns the content
def read_file(file):
    with open(file) as f:
        content = f.readlines()

    return content

# let us read the src file
file_contents = read_file("18.src")

# parse the file contents into our array/list structure
for index, line in enumerate(file_contents):
    global ORIGINAL_DATA
    # strip the new lines and trailing whitespaces
    l = file_contents[index].strip().split(" ")
    # convert the string to int
    l = map(int, l)
    # now append the line
    ORIGINAL_DATA.append( l )


# define all the necessary stuffs here
TOTAL_ROWS = len(ORIGINAL_DATA)
CURRENT_INDEX = TOTAL_ROWS
PREVIOUS_INDEX = CURRENT_INDEX - 1

# returns the max of (top + left) or (top + right)
# solves a triangle like below
#   2
# 1   3
# returns 5 in the above case
def solve_triangle(top, left, right):
    return max(top+left, top+right)

# solves the given list; called recursively
def solve():
    # use global values
    global ORIGINAL_DATA
    global CURRENT_INDEX
    global PREVIOUS_INDEX

    CURRENT_INDEX = CURRENT_INDEX - 1
    PREVIOUS_INDEX = CURRENT_INDEX - 1

    CURRENT_LINE = ORIGINAL_DATA[CURRENT_INDEX]
    PREVIOUS_LINE = ORIGINAL_DATA[PREVIOUS_INDEX]

    for index, elem in enumerate(PREVIOUS_LINE):
        x = index
        y = index + 1
        # calculate the triangle and replace the max as we traverse through the line
        top = PREVIOUS_LINE[index]
        left = CURRENT_LINE[x]
        right = CURRENT_LINE[y]

        PREVIOUS_LINE[index] = solve_triangle( top, left, right )

    # pop the last line
    ORIGINAL_DATA.pop()
    ORIGINAL_DATA[PREVIOUS_INDEX] = PREVIOUS_LINE

# solve the list 
for x in range(0, TOTAL_ROWS-1):
    solve()

print "final data ! ", ORIGINAL_DATA[0][0]


print time.time() - start_time, " seconds"



