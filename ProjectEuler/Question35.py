#First we find the permuations of a number
def get_permutations(s):
    if len(s) == 1:
        return [s]
    
    perms = []
    for i in range(len(s)):
        for p in get_permutations(s[:i] + s[i+1:]):
            perms.append(s[i] + p)
    return perms

def number_permutations(n):
    s = str(n)
    perms = get_permutations(s)
    return sorted(set(int(p) for p in perms))

#next we define a function to check if a number if prime (using code from question 7)
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


primes = []
LIMIT= pow(10, 6)

for number in range(0,LIMIT):
    perms = number_permutations(number)
    if all(isPrime(perm) for perm in perms):
        primes.append(number)

for number in primes:
    print (number)
numberCircular = len(primes)

print("The number of such primes is ", numberCircular)