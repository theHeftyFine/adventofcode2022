lines = open('input.txt').readlines()
total = 0

# Ugly pyhton is ugly. All you fancy linters probably kept perfectly handwritten notes in grade school

for line in lines:
    # split line in two
    l = len(line.strip())
    h = int(l/2)
    # save a line, more space for comments
    a,b = [line[0:h], line[h:l]]
    # keep track of items in set, for easy deduping
    common = set()
    # if an item exists in both half, keep it
    for ch in a:
        if ch in b:
            common.add(ch)
    for com in common:
        val = ord(com)
        # assume character is either in 'a-z' or 'A-Z'
        if val >= 97:
            total += val - 96
        else:
            total += (val - 64) + 26
print(total)