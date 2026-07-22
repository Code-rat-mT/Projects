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

for element in rotations:
    if element[0]=="L":
        elem1 = int(element[1:])
        location = location - elem1
        location = location % UPPER_LIMIT 
        if location == TARGET:
              zerocount+=1

    elif element[0] == "R":
        elem1 = int(element[1:])
        location = location + elem1
        location = location % UPPER_LIMIT 
        if location == TARGET :
              zerocount+=1
               
    print(location)
        
print(zerocount)




