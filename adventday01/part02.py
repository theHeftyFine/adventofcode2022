input = open("input01.txt", "r")
lines = input.readlines()
currentCal = 0;
highest = [];

for line in lines:
    try:
        currentCal = currentCal + int(line)
    except:
        highest.append(currentCal)
        currentCal = 0
        
highest.append(currentCal)
highest.sort(reverse=True)
highest = highest[0:3]
    
print(sum(highest))