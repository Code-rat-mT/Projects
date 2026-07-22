filelocation = "day4Input.txt"

lines = []
character = "@"

with open(filelocation, "r") as file:
    for line in file:
        lines.append(line.strip())

# Convert each line to list of chars
positions = [list(elem) for elem in lines]

rows = len(positions)
cols = len(positions[0])

neighbors = [
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
    (-1, -1),
    (-1,  1),
    ( 1, -1),
    ( 1,  1)
]

totalvalid = 0
running = True

while running:

    valid = 0               # <-- FIX: reset at start of loop
    to_remove = []          # store which positions to delete

    # SCAN PHASE
    for i in range(rows):
        for j in range(cols):

            if positions[i][j] == character:

                local_count = 0

                for dr, dc in neighbors:
                    nr = i + dr
                    nc = j + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if positions[nr][nc] == character:
                            local_count += 1

                if local_count < 4:
                    valid += 1
                    to_remove.append((i, j))
                    #store each positiong to be removed in an array

    # STOP CONDITION
    if valid == 0:
        running = False
        break

    # OUTPUT
    print("Forks to be lifted:", valid)
    totalvalid += valid

    # REMOVAL PHASE
    for r, c in to_remove:
        positions[r][c] = "."

    # PRINT GRID
    for row in positions:
        print("".join(row))
    print()

print("Total neighbor matches:", totalvalid)
