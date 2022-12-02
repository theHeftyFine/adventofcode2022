input = open('input.txt', 'r')
lines = input.readlines()
strategy = {
  'A': {'X': 3, 'Y': 6, 'Z': 0},
  'B': {'X': 0, 'Y': 3, 'Z': 6},
  'C': {'X': 6, 'Y': 0, 'Z': 3}
}
scores = {'X': 1, 'Y': 2, 'Z': 3}

total = 0

for line in lines:
    a, b = line.split()
    total = total + strategy[a][b] + scores[b]
    
print(total)