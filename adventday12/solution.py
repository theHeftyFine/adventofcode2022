def print_maze(maze):
    print('  ' + ' '.join(map(lambda d: map_int(d), list(range(0, len(maze[0]))))))
    
    for i in range(0, len(maze)):
        c = str(i)
        if len(c) < 2:
            c = '0' + c
        print(c + ' ' + '  '.join(maze[i]))

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
        
# 'First In First Out' Queue
class Fifo:    

    def __init__(self):
        self.content = []
    
    def push(self, elem):
        self.content.append(elem)
        
    def pop(self):
        elem = self.content[0]
        self.content = self.content[1:len(self.content)]
        return elem
        
    def has_elements(self):
        return len(self.content) > 0
        
# A Node represents one step in a path
class Node:

    def __init__(self, parent, coords, map):
        self.parent = parent
        self.x = coords[1]
        self.y = coords[0]    
        
        self.coords = coords
        self.s = map[coords[0]][coords[1]]
        self.path = [] if parent == None else parent.path + [(parent.y, parent.x)]   
        
        self.height = get_char_height(self.s)
        
    def __str__(self):
        return f"x: {self.x}, y: {self.y}, symbol: {self.s}, path length: {len(self.path)}"
        
    def gen_successors(self, map, succ_fun):
        successors = []
        x = self.x
        y = self.y
        
        for c in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            h, w = c
            if h >= 0 and w >= 0 and h < len(map) and w < len(map[0]) and succ_fun(get_char_height(map[h][w]), self.height):
                successors.append(Node(self, (h, w), map))
        
        return successors
        
def map_int(val):
    c = str(val)
    if len(c) < 2:
        return '0' + c
    return c
        
def breadth_first(node, endpoint, succ_fun):    
    queue = Fifo()
    queue.push(node)
    visited = [node.coords]
    
    while queue.has_elements():
        current_node = queue.pop()
        
        if current_node.s == endpoint:
            return current_node
        for child in current_node.gen_successors(maze, succ_fun):
            if child.coords not in visited:
                visited.append(child.coords)
                queue.push(child)
    return current_node
            
def search_and_calc_length(coords, end, fun):
    local_maze = [[c for c in line.strip()] for line in open('input.txt').readlines()]

    end = breadth_first(Node(None, coords, local_maze), end, fun)
        
    node = end

    while node is not None:
        local_maze[node.y][node.x] = '#'
        node = node.parent
        
    local_maze[coords[0]][coords[1]] = 'S'
    local_maze[end.y][end.x] = 'E'
                
    print_maze(local_maze)
        
    return len(end.path)
    
# Calc start and end points
maze = [[c for c in line.strip()] for line in open('input.txt').readlines()]

start_coords = (0, 0)
end_coords = (0, 0)

for y in range(0, len(maze)):
    for x in range(0, len(maze[y])):
        if maze[y][x] == 'S':
            start_coords = (y,x)
        if maze[y][x] == 'E':
            end_coords = (y,x)
    
fun_can_move_to = lambda target, source: target <= source + 1
fun_could_move_from = lambda source, target: target <= source + 1
    
# Shortest route from S to (any) E
print('solution 01', search_and_calc_length(start_coords, 'E', fun_can_move_to))

# Shortest route from E to (any) a
print('solution 02', search_and_calc_length(end_coords, 'a', fun_could_move_from))