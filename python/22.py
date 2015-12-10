import time

start_time = time.time()

ALPHABETS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# keeps tracl of the final score
SCORES = 0

# reads a file and returns the content
def read_file(file):
    with open(file) as f:
        content = f.read()

    return content

# let us read the src file
file_contents = read_file("p022_names.txt")

names = sorted(file_contents.split(","))

# strip the quotes
names = [name[1:-1]  for name in names]

for index, name in enumerate(names):

    # find the weight of the name
    letters = list(name)

    WEIGHT = 0

    for l in letters:
        WEIGHT = WEIGHT + ALPHABETS.index(l) + 1

    # add the score of this name
    score = WEIGHT * (index + 1)
    SCORES = SCORES + score

print "SCORE IS : ", SCORES

print time.time() - start_time, " seconds"