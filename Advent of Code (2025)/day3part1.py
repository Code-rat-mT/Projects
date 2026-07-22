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

joltages = []
largest1 = 0
largest2 = 0
indexofLargest1 = 0
indexofLargest2 = 0
counter = 0

#I only find the largest element twice

for array in wholelist:
    largest1 = 0
    largest2 = 0
    indexofLargest1 = 0
    indexofLargest2 = 0
    for i in range(len(array)-1):
        if array[i]> largest1:
            largest1 = array[i]
            indexofLargest1 = i

    array = array[indexofLargest1+1:]


    for i in range(len(array)):
        if array[i]> largest2:
            largest2 = array[i]
            indexofLargest2 = i

    number = str(largest1) + str(largest2)
    joltages.append(int(number))

print(joltages)

sum = 0
for jolt in joltages:
    sum+=jolt

print(sum)





