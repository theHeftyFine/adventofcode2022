lines = open("input.txt").readlines()

global pixels
pixels = ''

x = 1
execution = None
global total
total = 0

cycle = 1

def inc_and_check(cycle):
    global total
    global pixels
    # add to total when cycle at these points
    if cycle in [20, 60, 100, 140, 180, 220]:
        total += cycle * x
    # cycle 1 starts at pixel 0, so subtract 1
    if cycle - 1 <= 240 and (cycle - 1) % 40 in [x - 1, x, x +1]:
        pixels += '#'
    else:
        pixels += '.'
    return cycle + 1

for line in lines:
    try:
        # add to register command
        op, val = line.strip().split()
        # we don't actually execute the next command untill the last one finished
        # so when we encounter addx, skip two cycles, checking each cycle
        # and add to the register at the end of the second one
        cycle = inc_and_check(cycle)
        cycle = inc_and_check(cycle)
        x += int(val)
    except:
        # noop
        # pass a cycle and increment
        cycle = inc_and_check(cycle)
    
print('solution 1:', total)
print('solution 2:')
print(pixels[0:40])
print(pixels[40:80])
print(pixels[80:120])
print(pixels[120:160])
print(pixels[160:200])
print(pixels[200:240])