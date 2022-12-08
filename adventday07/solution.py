input = open('input.txt')

result = []

results = {}

# Bad, bad, bad, nasty, diry code OvO
   
def read_dir(dir):
    out = try_command(input.readline(), dir)
    result.append((dir, out[1]))
    if dir in results:
        results[dir] += out[1]
    else:
        results[dir] = out[1]
    return out
    
def list_files():
    files = []
    line = input.readline()
    terms = line.split(' ')
    while line != '' and terms[0] != '$':
        if terms[0] != 'dir':
            files.append(int(terms[0]))
        line = input.readline()
        terms = line.split(' ')
    return (line, sum(files))

def try_command(last_line, last_dir):
    results = []
    back = False
    line = last_line
    
    while line != '' and not back:
        terms = line.split(' ')
        if len(terms) > 0 and terms[0] == '$':
            if terms[1] == 'cd':
                dir = terms[2].strip()
                if dir == '..':
                    line = input.readline()
                    back = True
                else:
                    result = read_dir(dir)
                    line = result[0]
                    results.append(result[1])
            elif terms[1].strip() == 'ls':
                result = list_files()
                line = result[0]
                results.append(result[1])
        else:
            line = input.readline()
    return (line, sum(results))
    

try_command(input.readline(), '')

total_1 = 0
total_2 = ('', 40_000_000)

print(results)

for dir, value in results.items():
    if value <= 100_000:
        total_1 += value
    print(dir, value)
    if value >= 30_000_000 and value <= total_2[1]:
        total_2 = (dir, value)
        
print('result 01', total_1)
print('result 02', total_2)