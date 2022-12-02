input = open('input.txt', 'r')
lines = input.readlines()
strategy = {
  'A': {'X': 3, 'Y': 1, 'Z': 2},
  'B': {'X': 1, 'Y': 2, 'Z': 3},
  'C': {'X': 2, 'Y': 3, 'Z': 1}
}
scores = {'X': 0, 'Y': 3, 'Z': 6}

total = 0

for line in lines:
    a, b = line.split()
    total = total + strategy[a][b] + scores[b]
    
print(total)