filelocation = "day2Input.txt"

# Read file as one large string
with open(filelocation, "r") as file:
    content = file.read()

def checksequence(number):
    s = str(number)
    L = len(s)

    # Try all possible repetition counts (2 to L)
    for k in range(2, L + 1):
        if L % k != 0:
            continue  # must divide evenly

        chunk_len = L // k
        chunk = s[:chunk_len]

        # Prevent sequences like "0101"
        if chunk[0] == '0':
            continue

        # Check if repeating chunk k times gives the number
        if chunk * k == s:
            return True

    return False


# Parse input
ranges = content.split(",")

invalids = []
total_sum = 0

for r in ranges:
    start, end = map(int, r.split("-"))
    for n in range(start, end + 1):
        if checksequence(n):
            invalids.append(n)
            total_sum += n

print(invalids)
print(total_sum)
