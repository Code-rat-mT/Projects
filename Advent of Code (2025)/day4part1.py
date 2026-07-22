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

forkliftcount = 0

# DIRECTION OFFSETS: (row_offset, col_offset)
neighbors = [
    (-1,  0),  # up
    ( 1,  0),  # down
    ( 0, -1),  # left
    ( 0,  1),  # right
    (-1, -1),  # diag up-left
    (-1,  1),  # diag up-right
    ( 1, -1),  # diag down-left
    ( 1,  1)   # diag down-right
]

valid = 0

for i in range(rows):
    for j in range(cols):

        # Check if THIS position is the character
        if positions[i][j] == character:

            local_count = 0

            # Check all 8 neighbors
            for dr, dc in neighbors:
                nr = i + dr
                nc = j + dc

                # Check boundaries before accessing
                if 0 <= nr < rows and 0 <= nc < cols:
                    if positions[nr][nc] == character:
                        local_count += 1
            if local_count < 4:
                 valid += 1

            forkliftcount += local_count
    

print("Total neighbor matches:", valid)
