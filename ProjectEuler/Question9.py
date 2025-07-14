limit = 1000
triples = []
#I use a brute force to test all possible values
for a in range(1, limit):
    for b in range(a + 1, limit):  
        c = limit - a - b
        if c > 0 and a**2 + b**2 == c**2:
            print("Solution found! The triplet is:", a, b, c)
            print("The product is:", a * b * c)
            triples.append((a, b, c))
