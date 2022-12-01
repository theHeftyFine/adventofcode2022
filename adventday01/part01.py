input = open("input01.txt", "r")
lines = input.readlines()
currentCal = 0;
highest = 0;

for line in lines:
    try:
        currentCal = currentCal + int(line)
    except:
        highest = highest if highest > currentCal else currentCal
        currentCal = 0
        
highest = highest if highest > currentCal else currentCal

print(highest)