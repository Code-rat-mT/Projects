number = int(input("Enter a number: "))

def modulo(number, n):

    return (number % n == 0)

n = 1
quotient = 0
factors = []

while number>1:
    if modulo(number, n):
        number = number/n
        factors.append(n)
        n=2
    else:
        n=n+1


print(factors)
