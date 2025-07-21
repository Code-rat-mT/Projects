def findProperDivisors(number):
    divisors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            if i != 1 and i != number // i:
                divisors.add(number // i)
    divisors.discard(number)  # Remove the number itself
    return divisors

limit = 10000
amicable = []

for number in range(2, limit):
    sum1 = sum(findProperDivisors(number))
    if sum1 != number:
        sum2 = sum(findProperDivisors(sum1))
        if sum2 == number:
            pair = tuple(sorted((number, sum1)))
            if pair not in amicable:
                amicable.append(pair)

print("Amicable pairs under", limit, ":", amicable)

sum = 0
for number1, number2 in amicable:
       sum+=number1
       sum+=number2

print(sum)
