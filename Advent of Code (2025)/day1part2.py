#first step we will get the input from a text file
filelocation = "day1Input.txt"
rotations = [] #I make a list of the rotations and each line will be an element of the list

with open(filelocation, "r") as file:
    content = file.readlines()

#I make a list of the rotations from the file
for line in content:
    rotations.append(line.strip())

#50 is the start point left will be substraction and right will be addition
location = 50 
LOWER_LIMIT = 0
UPPER_LIMIT = 100
TARGET = 0
zerocount = 0
step = 1 #will analyze everything step by step

for element in rotations:
    location = location%UPPER_LIMIT
    if element[0]=="L":
        elem1 = int(element[1:])
        for _ in range(elem1):
            location = (location - step)%100
            if location == 0:
                zerocount+=1
        #if while moving left we encounter zero, then we add to the zero count
        
    elif element[0] == "R":
        elem1 = int(element[1:])
        for _ in range(elem1):
            location = (location + step)%100
            if location  == 0:
                zerocount+=1
        #if while moving right we encounter zero, then we add to the zero count
               
        
print(zerocount)




