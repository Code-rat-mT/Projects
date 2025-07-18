
def findDivisors(number):
    divisors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return divisors

# Function to generate the nth triangle number
def triangleN(n):
    return n * (n + 1) // 2

count = 1
while True:
    tri = triangleN(count)
    divisors = findDivisors(tri)

    if len(divisors) > 500:
        print("The triangle number with over 500 divisors is:", tri)
        break

    count += 1
