with open("inputs/day10.txt" , "r") as f:
    input = [[s[0:4], int(s[5:] or 0)] for s in f.read().split("\n")]

#part 1
cycle = 0
x = 1
sol = {0:1}

for (instr, n) in input:
    if instr == "noop":
        cycle += 1
        sol[cycle] =  x
    else:
        cycle += 2
        sol[cycle-1] = x
        sol[cycle] =  x
        x += n

sol1 = sol[20]*20 + sol[60]*60 + sol[100]*100 + sol[140]*140 + sol[180]*180 + sol[220]*220
print(sol1)
    
#part2
screen = [['░' for x in range(40)] for y in range(6)]

for cycle in range(240):
    x = cycle % 40
    sprite = sol[cycle+1] 
    sprite_pos = [sprite-1, sprite, sprite+1]
    if x in sprite_pos:
        row = cycle // 40
        col = cycle % 40
        screen[row][col] = '█'


for line in screen:
    print("".join(line))
