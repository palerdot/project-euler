import time

start_time = time.time()

# the points in each direction in the path
# this is for a 20 * 20 grid
ROWS = 20
COLS = 20

# # NOTE: I came up with the below formula which seemed to work fine, but was not accurate enough
# # TODO: Come back later and try to understand the actual math behind this problem

# DOWN_PATH = (ROWS - 2) * (COLS - 1)
# RIGHT_PATH = (COLS - 2) * (ROWS - 1)

# TOTAL_PATHS = RIGHT_PATH + DOWN_PATH + 2

def fact(n):
	if (n < 2):
		return n
	else:
		return n * fact(n-1)

def calculate_paths(ROWS, COLS):
	# total paths in right and down direction will be given by following formula
	TOTAL_PATHS = (fact(ROWS + COLS))/(fact(ROWS) * fact(COLS))

	return TOTAL_PATHS

PATHS = calculate_paths(ROWS, COLS)

print "possible paths ", PATHS

print time.time() - start_time, " seconds"