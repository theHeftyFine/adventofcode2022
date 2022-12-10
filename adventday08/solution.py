from os import system
from time import sleep

lines = open("input.txt").readlines()

forest = []

def visible_north(i, j):
    size = forest[i][j]
    dist = 0
    n = i - 1;
    visible = True
    while visible == True and n > -1:
        visible = forest[n][j] < size
        dist += 1
        n -= 1
    return (visible, dist)
    
def visible_south(i, j):
    size = forest[i][j]
    dist = 0
    s = i + 1;
    visible = True
    while visible == True and s < len(forest):
        visible = forest[s][j] < size
        dist += 1
        s += 1
    return (visible, dist)
    
def visible_west(i, j):
    size = forest[i][j]
    dist = 0
    w = j - 1;
    visible = True
    while visible == True and w > -1:
        visible = forest[i][w] < size
        dist += 1
        w -= 1
    return (visible, dist)
    
def visible_east(i, j):
    size = forest[i][j]
    dist = 0
    row = forest[i]
    e = j + 1;
    visible = True
    while visible == True and e < len(row):
        visible = forest[i][e] < size
        dist += 1
        e += 1
    return (visible, dist)


for line in lines:
    trees = []
    for tree in line.strip():
        trees.append(int(tree))
    forest.append(trees)

count = (2*len(forest)) + (2*(len(forest[0]) - 2))

internal_count = 0
internal_count_alt = 0
    

for i in range(0, len(forest) - 1):
    treeline = forest[i]
    for j in range(0, len(treeline) - 1):
        if i != 0 and j != 0 and i != len(forest) - 1 and j != len(treeline) - 1:
            visible = visible_north(i, j)[0] or visible_south(i, j)[0] or visible_west(i, j)[0] or visible_east(i, j)[0]
            if visible:
                internal_count += 1
                
print('solution_01', count + internal_count)

prettiest_tree = 0

for i in range(0, len(forest) - 1):
    treeline = forest[i]
    for j in range(0, len(treeline) - 1):
        decor = visible_north(i, j)[1] * visible_south(i, j)[1] * visible_west(i, j)[1] * visible_east(i, j)[1]
        if decor > prettiest_tree:
            prettiest_tree = decor
            
print('solution_02', prettiest_tree)