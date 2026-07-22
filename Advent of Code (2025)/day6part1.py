filelocation = "day6Input.txt"

lines = []

with open(filelocation, "r") as file:
    for line in file:
        lines.append(line.strip())

mylines = [] #this will store items horizontally
listvertical = []
# I make a vertical list

for line in lines:
    mylines.append(line.split(" "))


for line in mylines:
    while "" in line:
     line.pop(line.index("")) #On here I just remove all empty spaces while they are in the line



for i in range(len(mylines[0])):
    templist= []
    for j in range(len(mylines)):
       templist.append(mylines[j][i]) # I switch up the indexes to read vertically instead of horitally
    listvertical.append(templist)

#retrieve the vertical list to horizontal

total = 0

for listH in listvertical:
    operator = listH[-1]
    listH.pop(-1)
    sum = 0
    product = 1

    for elem in listH:
        if operator == "*":
            product *= int(elem) 
        elif operator == "+":
            sum += int(elem)
        
    if operator == "*":
        total +=product
    elif operator == "+":
        total +=sum

print("The total sum of products and sums is ", total)