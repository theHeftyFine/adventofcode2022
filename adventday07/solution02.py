import json

input = open("input.txt")

# note: size tree can be stored in nested array, but dictionary is more fun

# build directory tree
# dir = current directory, dir_name = name of the directory
def process_dir(dir, dir_name):
    # keep running total size of current dir, no need to calculate twice
    sum = 0
    # read next line
    line = input.readline().strip()
    # continue until end of input, or if a command to go up a directory is detected
    while line != '$ cd ..' and line != '':
        terms = line.split(' ')
        if len(terms) > 0:
            # if current line starts with '$ cd', process subdirectory (command 'cd ..' is already excluded)
            if terms[0] == '$':
                if terms[1] == 'cd':
                    next_dir = terms[2]
                    # initialize dict for current directory, if not present
                    if terms[1] not in dir:
                            dir[terms[1]] = {}
                    # process subdirectory recursively, and store result in current directory
                    dir[next_dir] = process_dir(dir[next_dir], next_dir)
                    # the total size of the subdirectory is added to the running total size of the current directory
                    sum += dir[next_dir]['_sum']
            # since 'cd' commands already detect subdirectories, 'ls' commands are redundant
            else:
                try:
                    # try parsing the first term as an integer. This indicates a line with a file size, followed by the file
                    value = int(terms[0])
                    # add file size to running total size of current dir
                    sum += value
                except:
                    pass
                # since 'cd' commands already detect subdirectories, other file lines (namely 'dir'), are redundant
        # read next line
        line = input.readline().strip()
        
    # the '_sum' property indicates the total size of the current file
    # it should not already exist, but just to be safe, add the running total size to the current total size, or just set it if absent
    if '_sum' not in dir:
        dir['_sum'] = 0
    dir['_sum'] += sum
    return dir
    
# calculate sum of the size of all subdirectories with a size of at most 100_000
# dir = current directory
def sum_atmost_100_000(dir):
    total = 0
    for key, val in dir.items():
        # add size of current directory if smaller than 100_000
        if key == '_sum':
            if val <= 100_000:
                total += val
        else:
            # add the same for subdirectories, recursively
            total += sum_atmost_100_000(val)
    return total
    
# Calculate smallest directory to be removed in order to free up enough space
# name = name of current directory, dir = current directory, space = space to free up
def min_dir_above_30_000_000(name, dir, space):
    # in lack of further knowledge, current dir is smallest
    # (also keep track of name of smallest directory, for extra Fun Points™)
    min = (name, dir['_sum'])
    for key, val in dir.items():
        # only interested in subdirectories
        if key != '_sum':
            # recursively determine smallest sub directory that is larger or equal to space to free up
            next_dir, value = min_dir_above_30_000_000(key, val, space)
            # if smallest subdirectory has the right size, and is smaller than the current known minimum, make it the new minimum
            if value >= space and value < min[1]:
                min = (next_dir, value)
    return min
    
# skip first line
input.readline()

result = process_dir({}, '/')

# pretty print calculated directory tree, for even more Fun Points™
print(json.dumps(result, indent=2, sort_keys=True))

print('solution01:', sum_atmost_100_000(result))

root_space = result['_sum']
space_left = 70_000_000 - root_space
space_needed = 30_000_000 - space_left

print('solution02:', min_dir_above_30_000_000('/', result, space_needed))

