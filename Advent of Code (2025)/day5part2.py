filelocation = "day5Input.txt"

lines = []

with open(filelocation, "r") as file:
    for line in file:
        lines.append(line.strip())

indexOfBlanck = lines.index("")

ranges = lines[:indexOfBlanck]

intervals = []

# Parse ranges into interval tuples
for r in ranges:
    start, end = map(int, r.split("-"))
    intervals.append((start, end))

# Sort intervals
intervals.sort()

# Merge overlapping or touching ranges
merged = []
for s, e in intervals:
    if not merged or s > merged[-1][1] + 1:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

# Count total allowed numbers
total_allowed = sum(e - s + 1 for s, e in merged)

print("The number of allowed ingredients is", total_allowed)
