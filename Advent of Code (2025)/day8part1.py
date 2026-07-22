from itertools import combinations

# -----------------------------
# Config
# -----------------------------
FILE = "day8Input.txt"        # change to your input file
TARGET_CONNECTIONS = 10    # set to 10 to reproduce the example's "after 10 connections" behavior

# -----------------------------
# 1) Read coordinates
# -----------------------------
coords = []
with open(FILE, "r") as f:
    for line in f:
        s = line.strip()
        if not s:
            continue
        coords.append(list(map(int, s.split(","))))

n = len(coords)
if n == 0:
    raise SystemExit("No coordinates found in file.")

# -----------------------------
# 2) Build all pairs with squared distance
# -----------------------------
pairs = []
# store (squared_distance, i, j) — sorting uses i/j as deterministic tie-breaker
for (i, p1), (j, p2) in combinations(enumerate(coords), 2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    dist2 = dx*dx + dy*dy + dz*dz
    pairs.append((dist2, i, j))

pairs.sort(key=lambda x: (x[0], x[1], x[2]))  # deterministic sort

# -----------------------------
# 3) Union-Find (Disjoint Set)
# -----------------------------
parent = list(range(n))
size = [1] * n

def find(x):
    # path compression
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    # union by size
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

# -----------------------------
# 4) Process pairs until TARGET_CONNECTIONS successful unions
# -----------------------------
connections = 0
for dist2, a, b in pairs:
    if union(a, b):
        connections += 1
    if connections >= TARGET_CONNECTIONS:
        break

# -----------------------------
# 5) Collect final component sizes
# -----------------------------
for i in range(n):
    parent[i] = find(i)

comp_counts = {}
for i in range(n):
    r = parent[i]
    comp_counts[r] = comp_counts.get(r, 0) + 1

sizes = sorted(comp_counts.values(), reverse=True)

# Ensure we have at least three components (pad with 1s if necessary)
while len(sizes) < 3:
    sizes.append(1)

result = sizes[0] * sizes[1] * sizes[2]

print(f"Total points: {n}")
print(f"Successful connections made: {connections}")
print("Top 3 component sizes:", sizes[:3])
print("Product of top 3 sizes:", result)
