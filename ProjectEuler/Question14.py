def collatz(start):
    collaz = [start]
    while start != 1:
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
        collaz.append(start)
    return collaz

collaz_lengths = []
LIMIT = 10**6

for number in range(1, LIMIT):
    sequence = collatz(number)
    collaz_lengths.append(len(sequence))

max_length = max(collaz_lengths)
starting_number = collaz_lengths.index(max_length) + 1  

print(f"Longest Collatz sequence under {LIMIT} is produced by {starting_number} with length {max_length}")
