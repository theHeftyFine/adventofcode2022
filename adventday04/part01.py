lines = open("input.txt").readlines()

total = 0

for line in lines:
    a,b = line.split(',')
    starta,enda = a.split('-')
    startb,endb = b.split('-')
    rangea = [*range(int(starta), int(enda) + 1)]
    rangeb = [*range(int(startb), int(endb) + 1)]
    
    ainb = []
    for ap in rangea:
        if ap not in rangeb:
            ainb.append(ap)
            
    bina = []
    for bp in rangeb:
        if bp not in rangea:
            bina.append(bp)
    
    if len(ainb) == 0 or len(bina) == 0:
        total += 1
print(total)