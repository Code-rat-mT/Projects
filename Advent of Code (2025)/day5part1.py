filelocation = "day5Input.txt"

lines = []
character = "@"

with open(filelocation, "r") as file:
    for line in file:
        lines.append(line.strip())

indexOfBlanck = lines.index("")

ranges = lines[:indexOfBlanck]
availableIngs = lines[indexOfBlanck+1:]


print(ranges)
print(availableIngs)

allowedranges = []

for rang in ranges:
    numbers = rang.split("-")
    for number in range(int(numbers[0]), int(numbers[1])+1):
        allowedranges.append(number)

freshIngredients = []

for value in availableIngs:
    if int(value) in allowedranges:
        print(value, " allowed ")
        freshIngredients.append(value)
    else:
        print("Spoiled")


fresh = len(freshIngredients)

print("The number of fresh ingredients is ", fresh)


# the above code is too slow