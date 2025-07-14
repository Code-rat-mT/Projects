#To find the sum of primes less than 2 million. For this one I modify 
#My solution to question 7 on finding primes
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

limit = 2*pow(10,6)
primes = []

for i in range(limit):
    if isPrime(i):
        primes.append(i)

sum = 0
#Then I just sum up all the primes
for prime in primes:
    sum += prime

print("The sum is ", sum)
