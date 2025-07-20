#We'll start with a function to find the factorial
def factorial(number):
    factor = number
    if (number == 1):
        return 1
    else:
        return factor * factorial(number-1)
    

limit = 100
number = factorial(limit)
sum = 0

print(number)

stringNumber = str(number)
listNumber = list(stringNumber)

print(listNumber)

for numb in listNumber:
    sum+=int(numb)

print(F"The sum of the numbers in is {limit}! is ", sum)

