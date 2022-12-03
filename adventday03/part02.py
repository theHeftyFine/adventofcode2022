lines = open('input.txt').readlines()
total = 0

# group data by threes
data = [lines[i:i+3] for i in range(0, len(lines), 3)]

# all I want for christmas is list destructuring in for loop expressions
for a, b, c in data:
    # collect badges in set for easy deduping
    common = set()
    for ch in a.strip():
        # Badge letter has to exist in all 3 bags, other items can only exist twice in a group
        if ch in b.strip() and ch in c.strip():
            common.add(ch)
    for com in common:
        val = ord(com)
        # just assume each char is either in 'A-Z' or 'a-z'
        if val >= 97:
            total += val - 96
        else:
            total += (val - 64) + 26
print(total)