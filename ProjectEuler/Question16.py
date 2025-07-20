#Power digit sum
limit = 1000
power = 2
number = 1
sum = 0

number = 2**limit

stringNumber = str(number)
listNumber = list(stringNumber)

print(listNumber)

for number in listNumber:
    sum+=int(number)

print("The sum of the numbers is ", sum)