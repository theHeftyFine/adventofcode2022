from os import system
import sys

global toprow

def print_maze(maze):
    print(toprow)
    
    for i in range(0, len(maze)):
        c = str(i)
        if len(c) < 2:
            c = '0' + c
        print(c + ' '.join(maze[i]))
        
def manhattan(x,y,i,j):
    return abs(x - i) + abs(y - j)
    
def euclid(coords, top):
    y = top[0] - coords[0]
    x = top[1] - coords[1]
    return x*x + y*y

def get_char_height(c):
    # assume end point is highest point on the map
    if c == 'E':
        return 123
    # assume start point is the lowest point on the map
    elif c == 'S':
        return 96
    # we only care about difference between tiles, so just use the char value
    else:
        return ord(c)
        
def can_move_up(coords, maze):
    y = coords[0]
    x = coords[1]
    h = get_char_height(maze[y][x])
    t = h + 1
    
    if y > 0 and get_char_height(maze[y-1][x]) == t:
        return True
    if y < len(maze) - 1 and get_char_height(maze[y+1][x]) == t:
        return True
    if x > 0 and get_char_height(maze[y][x-1]) == t:
        return True
    if x < len(maze[0]) - 1 and get_char_height(maze[y][x+1]) == t:
        return True
    return False
    
        
class Fifo:

    content = []
    
    def push(self, elem):
        self.content.append(elem)
        
    def pop(self):
        elem = self.content[0]
        self.content = self.content[1:len(self.content)]
        return elem
        
    def has_elements(self):
        return len(self.content) > 0
        
class Node:

    def __init__(self, parent, coords, end, map, dir):
        self.parent = parent
        self.x = coords[1]
        self.y = coords[0]
        self.coords = coords
        self.s = map[coords[0]][coords[1]]
        self.dir = dir
        self.path = [] if parent == None else parent.path + [(parent.y, parent.x)]
        
        # cost is one more than the last step
        self.g = parent.g + 1 if parent is not None else 1
        
        self.height = get_char_height(self.s)
        
    def __str__(self):
        return f"x: {self.x}, y: {self.y}, symbol: {self.s}, weight: {self.g}, distance: {self.h}, moved from parent: {self.dir}"
        
    def gen_successors(self, map, end):
        successors = []
        x = self.x
        y = self.y
        
        up = y - 1
        down = y + 1
        left = x - 1
        right = x + 1
        
        # we can move up or down, or stay on the same level, in respect to the current node, as long as the step is at most one
        h_range = [self.height - 1, self.height, self.height +1]
        
        # Up
        if up >= 0 and up < len(map) and get_char_height(map[up][x]) <= self.height + 1:
            successors.append(Node(self, (up, x), end, map, '^'))
        # Down
        if down >= 0 and down < len(map) and get_char_height(map[down][x]) <= self.height + 1:
            successors.append(Node(self, (down, x), end, map, 'V'))         
        # Left
        if left >= 0 and left < len(map[0]) and get_char_height(map[y][left]) <= self.height + 1:
            successors.append(Node(self, (y, left), end, map, '<'))
        # Right
        if right >= 0 and right < len(map[0]) and get_char_height(map[y][right]) <= self.height + 1:
            successors.append(Node(self, (y, right), end, map, '>'))        
        
        return successors
        
def map_int(val):
    c = str(val)
    if len(c) < 2:
        return '0' + c
    return c
        
def breadth_first(node, endpoint = 'E'):    
    queue = Fifo()
    queue.push(node)
    visited = [node.coords]
    step = 0
    
    path_lengths = []
    
    while queue.has_elements():
        current_node = queue.pop()
        
        system('cls')
    
        maze[current_node.y][current_node.x] = '@'
    
        print('depth', len(current_node.path))
        print('elements in queue', len(queue.content))
        print('step', step)
    
        print_maze(maze)
        
        maze[current_node.y][current_node.x] = current_node.s
        
        if current_node.s == endpoint:
            return current_node
        for child in current_node.gen_successors(maze, end_coords):
            if child.coords not in visited:
                visited.append(child.coords)
                queue.push(child)
                
        step += 1
    return current_node

maze = [[c for c in line.strip()] for line in open('input.txt').readlines()]

toprow = ' ' + ''.join(map(lambda d: map_int(d), list(range(0, len(maze[0])))))

start_coords = (0, 0)
end_coords = (0, 0)

for y in range(0, len(maze)):
    for x in range(0, len(maze[y])):
        if maze[y][x] == 'S':
            start_coords = (y,x)
        if maze[y][x] == 'E':
            end_coords = (y,x)
    

end = breadth_first(Node(None, start_coords, end_coords, maze, 'Start'))

# system('cls')

# print_maze(maze)
    
node = end

first_a_found = False

steps = 0

while node is not None:
    maze[node.y][node.x] = '#'
    node = node.parent
    if not first_a_found:
        if node.s == 'a':
            first_a_found = True
            start = node
        else:
            steps += 1
            
print_maze(maze)
    
print('solution 01:', len(end.path))

valid_starts = []

for i in range(0, len(maze)):
    for j in range(0, len(maze[i])):
        if maze[i][j] == 'a' and can_move_up((i,j), maze):
            valid_starts.append((i,j))

print(len(valid_starts))

starts_not_covered = [s for s in valid_starts if s not in end.path]

print(len(starts_not_covered))