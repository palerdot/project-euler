import math
import time
#import operator # for getting max value

# note the time when we start our program execution
start_time = time.time()

# define necessary paramters
ROWS = 20
COLUMNS = 20
# the distance in which we have to proceed in each direction
DISTANCE = 4


# directions: N, S, E, W, NE, NW, SE, SW
DIRECTIONS = ['N', 'S', 'E', 'W', 'NE', 'SE', 'SW']

# our data !
our_grid = [
    8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,
    49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0,
    81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,
    52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,
    22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,
    24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,
    32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,
    67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,
    24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,
    21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95,
    78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,
    16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57,
    86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,
    19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 4,
    4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,
    88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,
    4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,
    20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,
    20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,
    1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48
]

#our_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# directions array that contains the product of elements of our distance in all the directions
GRID_DIRECTIONS = []

# contains the product for all the directions for all the elements
MAX_PRODUCTS = []

# get index from row and column
def get_index(row, column):

    # if the row or column is out of range return -1
    if ( (row not in range(1, ROWS+1)) or (column not in range(1, COLUMNS+1)) ):
        return -1

    # else calculate the  index and return it
    return (row - 1)*COLUMNS + (column - 1)
# ^^ 

# for a given index returns the row and column for the array    
def get_row_col(index):
    # get the element
    elem = our_grid[index]
    # calculate row and column
    elem_row = (index / COLUMNS) + 1
    elem_col = (index % COLUMNS) + 1

    # return the row and column data
    return { 'row': elem_row, 'col': elem_col  }

#initialize the directions for each position with Nil value
def init_directions():

    # declare that we will be using our global directions
    global GRID_DIRECTIONS

    initial_template = {  
        'N': -1,
        'S': -1,
        'E': -1,
        'W': -1, 
        'NE': -1,
        'NW': -1,
        'SE': -1,
        'SW': -1
    }

    # first set the length of grid directions
    GRID_DIRECTIONS = [''] * len(our_grid)

    for i in range(0, len(our_grid)):
        # make a new copy of dictionary
        initial_directions = initial_template.copy()
        GRID_DIRECTIONS[i] = initial_directions

# calculate NORTH direction (TOP direction)
def calc_north(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 6 => row: 3, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    mirror_row = position['row'] - DISTANCE + 1
    mirror_column = position['col']
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if (row_not_valid or column_not_valid):
        # North direction not possible
        none_val = {
            'mirror_index': mirror_index,
            'direction': 'N',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }
        # stop execution here
        return none_val

    # north direction is possible; so let us proceed and calculate it
    
    # direction is north; so x decreases while y remains the same
    x_step = -1 # because x decreases
    x_coords = range( position['row'], mirror_row - 1, x_step )

    # y remains the same
    y_coords = [position['col']]*len(x_coords)

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'N',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculate SOUTH direction (DOWN direction)
def calc_south(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    mirror_row = position['row'] + DISTANCE - 1
    mirror_column = position['col']
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if (row_not_valid or column_not_valid):
        # South direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'S',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # south direction is possible; so let us proceed and calculate it
    
    # direction is south; so x increases while y remains the same
    x_step = 1 # because x increases
    x_coords = range( position['row'], mirror_row + 1, x_step )

    # y remains the same
    y_coords = [position['col']]*len(x_coords)

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'S',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculate EAST direction (RIGHT direction)
def calc_east(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    # row remains the same; column increases on the right
    mirror_row = position['row'] 
    mirror_column = position['col'] + DISTANCE - 1
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if ( row_not_valid or column_not_valid ):
        # East direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'E',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # East direction is possible; so let us proceed and calculate it
    
    # direction is East; so y increases while x remains the same
    y_step = 1 # because y increases
    # x remains the same
    x_coords = [position['row']] * DISTANCE
    # y increases
    y_coords = range( position['col'], mirror_column + 1, y_step )

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'E',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculate WEST direction (LEFT direction)
def calc_west(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    # row remains the same; column decreases to the left
    mirror_row = position['row'] 
    mirror_column = position['col'] - DISTANCE + 1
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if ( row_not_valid or column_not_valid ):
        # West direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'W',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # West direction is possible; so let us proceed and calculate it
    
    # direction is East; so y decreases while x remains the same
    y_step = -1 # because y decreases
    # x remains the same
    x_coords = [position['row']] * DISTANCE
    # y increases
    y_coords = range( position['col'], mirror_column - 1, y_step )

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'W',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# diagonal directions

# calculate NORTHEAST direction (TOP LEFT direction)
def calc_north_east(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    # row increases to the top; column increases to the right
    mirror_row = position['row'] - DISTANCE + 1
    mirror_column = position['col'] + DISTANCE - 1
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if ( row_not_valid or column_not_valid ):
        # NorthEast direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'NE',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # NorthEast direction is possible; so let us proceed and calculate it
    
    # direction is NorthEast; so x decreases; y increases
    # x decreases
    x_step = -1 
    x_coords = range( position['row'], mirror_row - 1, x_step )

    # y increases
    y_step = 1 
    y_coords = range( position['col'], mirror_column + 1, y_step )

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'NE',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculate NORTHWEST direction (TOP LEFT direction)
def calc_north_west(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    # row increases to the top; column decreases to the left
    mirror_row = position['row'] - DISTANCE + 1
    mirror_column = position['col'] - DISTANCE + 1
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if ( row_not_valid or column_not_valid ):
        # NorthWest direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'NW',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # NorthWest direction is possible; so let us proceed and calculate it
    
    # direction is NorthWest; so x decreases; y decreases
    # x decreases
    x_step = -1 
    x_coords = range( position['row'], mirror_row - 1, x_step )

    # y decreases
    y_step = -1 
    y_coords = range( position['col'], mirror_column - 1, y_step )

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'NW',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculate SOUTHEAST direction (BOTTOM RIGHT direction)
def calc_south_east(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    # row decreases to the bottom; column decreases to the left
    mirror_row = position['row'] + DISTANCE - 1
    mirror_column = position['col'] + DISTANCE - 1
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if ( row_not_valid or column_not_valid ):
        # South East direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'SE',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # South West direction is possible; so let us proceed and calculate it
    
    # direction is South West; so x decreases; y decreases
    # x increases
    x_step = 1 
    x_coords = range( position['row'], mirror_row + 1, x_step )

    # y increases
    y_step = 1 
    y_coords = range( position['col'], mirror_column + 1, y_step )

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'SE',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculate SOUTH WEST direction (BOTTOM LEFT direction)
def calc_south_west(index, mirror_dir):

    global DISTANCE
    global ROWS, COLUMNS

    # sample index: 0 => row: 1, column 1
    position = get_row_col(index)

    # calculate the mirror row, col and index
    # row increases to the bottom; column decreases to the left
    mirror_row = position['row'] + DISTANCE - 1
    mirror_column = position['col'] - DISTANCE + 1
    mirror_index = get_index(mirror_row, mirror_column)

    row_not_valid = (mirror_row not in range(1, ROWS + 1))
    column_not_valid = (mirror_column not in range(1, COLUMNS + 1))

    if ( row_not_valid or column_not_valid ):
        # South East direction not possible
        return {
            'mirror_index': mirror_index,
            'direction': 'SW',
            'mirror_direction': mirror_dir,
            'product': False # product not possible
        }

    # South West direction is possible; so let us proceed and calculate it
    
    # direction is South West; so x decreases; y decreases
    # x increases
    x_step = 1 
    x_coords = range( position['row'], mirror_row + 1, x_step )

    # y decreases
    y_step = -1
    y_coords = range( position['col'], mirror_column - 1, y_step )

    # our final list of co-ordinates for north direction
    coords = []
    # now construct the co-ordinates
    for i in range(len(x_coords)):
        # take the x,y position
        coords.append( [x_coords[i], y_coords[i]] )

    # our final product will be held here
    PRODUCT = 1

    for pos in coords:
        # index of the element from the co-ordinate
        e_index = get_index(pos[0], pos[1])
        # actual element itself from the index
        PRODUCT = PRODUCT * our_grid[e_index]

    # return our final product for this direction
    calculated = {
        'mirror_index': mirror_index,
        'direction': 'SW',
        'mirror_direction': mirror_dir,
        'product': PRODUCT
    }

    return calculated

# calculates the product in the given direction and also its mirror opposite
# for eg: for index: 0, direction = 'S', for our distance of 2, the mirror is
#             index: 6, direction = 'N'
# returns False if the mirror direction is not possible in the grid
def calc_mirror_directions(i, d):
    # our global distance
    global DISTANCE
    # define the mirror directions
    DIRECTIONS = {
        'N': {
            'mirror_dir': 'S',
            'calc': calc_north
        },
        'S': {
            'mirror_dir': 'N',
            'calc': calc_south
        },
        'E': {
            'mirror_dir': 'W',
            'calc': calc_east
        },
        'W': {
            'mirror_dir': 'E',
            'calc': calc_west
        },
        'NE': {
            'mirror_dir': 'SW',
            'calc': calc_north_east
        },
        'NW': {
            'mirror_dir': 'SE',
            'calc': calc_north_west
        },
        'SE': {
            'mirror_dir': 'NW',
            'calc': calc_south_east
        },
        'SW': {
            'mirror_dir': 'NE',
            'calc': calc_south_west
        }
    }

    mirror_dir = DIRECTIONS[d]['mirror_dir']

    # call the direction function 
    return DIRECTIONS[d]['calc'](i, mirror_dir) 

def print_grid_directions():
    for index, det in enumerate(GRID_DIRECTIONS):
            print index , det 
    print "\n ******************************************** \n "

def init(): 
    global MAX_PRODUCTS
    # will init all the operations
    init_directions()

    for e_index, elem in enumerate(our_grid):
        for index, direction in enumerate(DIRECTIONS):
            #print "will calculate for index: %d and direction: %s %s" % (e_index, direction, GRID_DIRECTIONS[e_index][direction])
            dir_details = calc_mirror_directions(e_index, direction)
            product = dir_details['product']
            # if the grid position for this direction is not calculated
            if (GRID_DIRECTIONS[e_index][direction] == -1):
                GRID_DIRECTIONS[e_index][direction] = product

                # if product is present update details for the mirror
                if (product != False):
                    mirror_index = dir_details['mirror_index']
                    mirror_direction = dir_details['mirror_direction']
                    GRID_DIRECTIONS[mirror_index][mirror_direction] = product

                # update the product to max product
                MAX_PRODUCTS.append(product) 

def get_max_value():
    
    # MAX = []
    # # ref: http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    # for i, dict in enumerate(GRID_DIRECTIONS):
    #     max_value = max(dict.iteritems(), key=operator.itemgetter(1))[1]
    #     #print max_value
    #     MAX.append(max_value)

    print max(MAX_PRODUCTS)

# initialize the program
init()
get_max_value()

# calculate the total time to run the program
total_time = time.time() - start_time

print "Time taken is %s seconds" % total_time
