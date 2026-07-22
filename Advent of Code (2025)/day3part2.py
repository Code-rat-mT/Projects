filelocation = "day3Input.txt"

lines  = []

with open(filelocation, "r") as file:
    content = file.readlines()

for line in content:
    lines.append(line.strip())

#I turn each line into a list
wholelist = []
for elem in lines:
    linearray = list(elem)
    templist = []
    for number in linearray:
        templist.append(int(number))
    wholelist.append(templist)

NUMBERLENGTH = 12
joltages = []
largest1 = 0
largest2 = 0
indexofLargest1 = 0
indexofLargest2 = 0
counter = 0

#I only find the largest element twice







