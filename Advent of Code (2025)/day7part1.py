#I think I will just count the number of splitters should be able to give me many times the tychon will be split
#So I will read the file just like all other times

filelocation = "day7Input.txt"

lines = []
splitter = "^"
splittercount = 0

with open(filelocation, "r") as file:
    for line in file:
        lines.append(line.strip())

positions = [list(line) for line in lines]

rows = len(positions)
cols = len(positions[0])
visited = set()
seen = set()
# I will store the beam direction in a queue
begin  = 0

for i in range(cols):
    if positions[0][i] == "S":
        begin = i

from collections import deque

nodesbeam = deque([(0, begin)]) # I make a queue to store the starting location of the node

while nodesbeam:
    row, col = nodesbeam.popleft()
    nextrow = row + 1
    nextcol = col



    if nextrow >= rows or nextcol >=cols:
        continue #The loop will go back to the top

    state = (nextrow, nextcol)
    if state in visited:
        continue
    visited.add(state)

    if positions[nextrow][nextcol] == splitter:
        seen.add((nextrow, nextcol))

        nodesbeam.append((nextrow, nextcol+1))
        nodesbeam.append((nextrow, nextcol-1))
    else:
        nodesbeam.append((nextrow, nextcol))

print("Number of splitter beams is ", len(seen))

