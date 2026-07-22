def allowed(number):
    for low, high in allowedranges:
         if low<=number<=high:
             return True
    return False

filelocation = "day5Input.txt"

lines = []

with open(filelocation, "r") as file:
    for line in file:
        lines.append(line.strip())

indexOfBlanck = lines.index("")

ranges = lines[:indexOfBlanck]
availableIngs = lines[indexOfBlanck+1:]



allowedranges = []

for rang in ranges:
    start, end = map(int, rang.split("-")) #I store everything in a map
    allowedranges.append((start, end)) #I add the maps of ranges to the list

fresh = 0

for value in availableIngs:
    if allowed(int(value)):
        fresh +=1

print("number of fresh ingredients is ", fresh)


# the above code is too slow