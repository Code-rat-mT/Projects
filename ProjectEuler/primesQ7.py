#We write a function that checks if a number is prime
def isPrime(numb):
    if numb <= 1:
        return False
    if numb == 2:
        return True
    if numb % 2 == 0:
        return False

    for i in range(3, int(numb**0.5) + 1, 2):
        if numb % i == 0:
            return False
    return True


numbers = [] # we make an array to store the numbers
limit = int(input("Enter the limit prime number you want to end at: "))
print(limit, " prime")
count = 0
numb = 2

while (count < limit):
    if isPrime(numb):            #solution is to store all prime numbers and the answer is numbers[-1] (the last of those)
        numbers.append(numb)
        count = count + 1
    numb = numb + 1


limitPrime = numbers[-1]
print("The ", limit, "th prime is ", limitPrime)

