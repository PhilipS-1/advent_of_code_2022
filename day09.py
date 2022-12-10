import builtins

with open("inputs/day09.txt", "r") as f:
    input = [s.replace(" ", "") for s in f.read().split("\n")]

#part1
positions_visited = set()
position_t, position_h = (0,0), (0,0)

def update_position(pos: tuple[int, int], move: str) -> tuple[tuple[int, int], int]:
    dir = move[0]
    len = int(move[1:])
    if(len == 0):
        return pos
    if dir == "R":
        return (pos[0] + 1, pos[1]), len -1
    if dir == "L":
        return (pos[0] - 1, pos[1]), len -1
    if dir == "U":
        return (pos[0], pos[1] + 1), len -1
    if dir == "D":
        return (pos[0], pos[1] - 1), len -1

def calc_dist(pos_h, pos_t):
    x = pos_h[0]
    y = pos_h[1]
    possibles_positions = [(a,b) for a in range (x-1, x+2) for b in range (y-1, y+2)]
    if pos_t not in possibles_positions:
        return 2
    return 1

for move in input:
    dir = move[0]
    len = int(move[1:])
    while len > 0:
        position_h_prev = position_h
        position_h, len = update_position(position_h, dir + str(len))
        dist = calc_dist(position_h, position_t)
        if dist > 1:
            position_t = position_h_prev
            positions_visited.add(position_t)
    

print("part1: ", builtins.len(positions_visited))

#part2
positions_visited = set()
position_t, position_h = (0,0), (0,0)

rope = [(0,0) for x in range (10)]

def update_knot(h, t):
    #same row or col
    if t[1] == h[1]:
        if h[0] > t[0]:
            return (t[0]+1, t[1])
        return (t[0]-1, t[1])
    if t[0] == h[0]:
        if h[1] > t[1]:
            return (t[0], t[1]+1)
        return (t[0], t[1]-1)
    #move diag
    if h[0] < t[0] and h[1] < t[1]:
        return (t[0] -1, t[1]-1)
    if h[0] > t[0] and h[1] < t[1]:
        return (t[0] +1, t[1]-1)
    if h[0] < t[0] and h[1] > t[1]:
        return (t[0] -1, t[1]+1)
    if h[0] > t[0] and h[1] > t[1]:
        return (t[0] +1, t[1]+1)
    

for move in input:
    dir = move[0]
    len = int(move[1:])
    while len > 0:
        rope[0], len = update_position(rope[0], dir + str(len))
        for i in range(1,10,1):
            dist = calc_dist(rope[i-1], rope[i])
            if(dist > 1):
                rope[i] = update_knot(rope[i-1], rope[i])
        positions_visited.add(rope[9])


print("part2: ", builtins.len(positions_visited))

        