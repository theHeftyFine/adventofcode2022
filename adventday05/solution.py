lines = open("input.txt").readlines()

storage = []

for line in lines:
    if '[' in line:
        col = 0
        # read the complete crate pile definition
        # and store it's characters in a 2d array
        # one row per column
        for column in [line[i:i+4] for i in range(0, len(line), 4)]:
            value = column[1]
            if len(storage) < col + 1:
                storage.append([])
            if value != ' ':
                storage[col].append(value)
            col += 1

def sort_input(reverse = True):
    loc_storage = storage.copy()

    for line in lines:
        if 'move' in line:
            parts = line.split(' ')
            # check if our instruction line has the expected amount of words
            # probably redundant
            if len(parts) == 6:
                # amount to move
                amount = int(parts[1])
                # column to pull from (index is minus 1)
                source = int(parts[3]) - 1
                # column to add to (index is minus 1)
                target = int(parts[5]) - 1
                
                # first <amount> items of <source> column
                take = loc_storage[source][0:amount]
                # The CrateMover 9001 moves all crates at once!
                # All this means is the crates will be added to the target column
                # in the order they were in the source column
                if reverse:
                    take.reverse()
                # new <source> column is old <source> column without first <amount> items
                loc_storage[source] = loc_storage[source][amount:len(loc_storage[source])]
                # new <target> column is <take> crates concatenated with old <target> column
                loc_storage[target] = take + loc_storage[target]

    toprow = ''
    for col in loc_storage:
        if len(col) > 0:
            toprow += col[0]
    return toprow
        
print('part01', sort_input())
print('part02', sort_input(False))