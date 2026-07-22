filelocation = "day7Input.txt"

# Load grid
grid = [list(line.strip("\n")) for line in open(filelocation)]
rows = len(grid)
cols = len(grid[0])

# Find starting S
for j in range(cols):
    if grid[0][j] == "S":
        start_col = j

# Beam simulation
from collections import deque
beams = deque([(0, start_col)])  # starting row = 0
touched_splitters = set()

while beams:
    r, c = beams.popleft()

    # next position is one row down
    nr = r + 1
    nc = c

    # Stop if out of bounds
    if nr >= rows or nc < 0 or nc >= cols:
        continue

    state = (nr, nc)
    if state in visited:
        continue
    visited.add(state)


    cell = grid[nr][nc]

    # If it's a splitter
    if cell == "^":
        touched_splitters.add((nr, nc))

        # split left and right
        beams.append((nr, nc - 1))
        beams.append((nr, nc + 1))

    else:
        # normal beam continues straight down
        beams.append((nr, nc))

print("Number of splitters actually touched =", len(touched_splitters))
