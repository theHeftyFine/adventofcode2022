from time import sleep
from os import system

def draw_grid(touched, head, tail, min_y, max_y, min_x, max_x):
    adj_y = min_y * -1
    adj_x = min_x * -1
    grid = []
    for i in range(0, max_y + adj_y + 1):
        grid.append(['.'] * ((max_x + adj_x) + 1))
    
    for t in touched:
        grid[t[0] + adj_y][t[1] + adj_x] = '#'
        
    grid[head[0] + adj_y][head[1] + adj_x] = 'H'
    
    if grid[tail[0] + adj_y][tail[1] + adj_x] == 'H':
        grid[tail[0] + adj_y][tail[1] + adj_x] = 'B'
    else:
        grid[tail[0] + adj_y][tail[1] + adj_x] = 'T'
        
    grid[adj_y][adj_x] == 'S'
        
    for row in grid:
        print(''.join(row))
        
def sign(value):
    if value == 0:
        return 0
    elif value < 0:
        return -1
    else:
        return 1

lines = open('input.txt').readlines()

total = len(lines)

grid = [['s']]







def simulate(tails):
    min_y = 0
    max_y = 0

    min_x = 0
    max_x = 0

    head_y = 0
    head_x = 0
    
    tail = [(0,0)]
    
    result = {(0, 0)}
    step = 1
    for line in lines:
        system('cls')
        print(step, 'of', total)
        
        dir, s = line.strip().split()
        steps = int(s)
        
        # move head
        for i in range(0, steps):
            if dir == 'U':
                head_y -= 1
            elif dir == 'D':
                head_y += 1
            elif dir == 'L':
                head_x -= 1
            elif dir == 'R':
                head_x += 1
        
            for j in range(0, len(tail)):               
                y, x = tail[j]
                old_tail = (y, x)
                
                h_y = head_y
                h_x = head_x
                
                if len(tail) != 0 and j > 0:
                    h_y, hx = tail[j-1]
                    
                
                diff_y = head_y - y
                diff_x = head_x - x
                
                # in same column
                if diff_y == 0:
                    if diff_x == 2:
                        tail[j] = (y, x + 1)
                    elif diff_x == -2:
                        tail[j] = (y, x - 1)
                # in same row
                elif diff_x == 0:
                    if diff_y == 2:
                        tail[j] = (y + 1, x)
                    elif diff_y == -2:
                        tail[j] = (y - 1, x)
                # not touching
                elif abs(diff_y) == 2 or abs(diff_x) == 2:
                    tail[j] = (y + sign(diff_y), x + sign(diff_x))
                    
                # add to visited
                result.add((tail[j][0], tail[j][1]))
                if len(tail) < tails and old_tail != tail[j]:
                    tail.append(old_tail)

                
            min_y = head_y if head_y < min_y else min_y
            max_y = head_y if head_y > max_y else max_y
            min_x = head_x if head_x < min_x else min_x
            max_x = head_x if head_x > max_x else max_x  
        step += 1  
    return(result)
    
solution1 = len(simulate(1))
solution2 = len(simulate(9))

print('solution01', solution1)
print('solution02', solution2)
    