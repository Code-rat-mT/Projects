data = open("dataQ13.txt", "r")
input = []
for line in data.readlines():
    input.append(line.strip())

numberInput = []
for element in input:
    numberInput.append(int(element))

sum = 0

for element in numberInput:
    sum+=element

sumString = str(sum)
first10 = sumString[:10]
print(sum)
print(first10)