#part1
with open("inputs/day06.txt", "r") as f:
    input = f.read()

for (i, char) in enumerate(input[3:], start = 3):
    s = set(input[i-4:i])
    if(len(s) >= 4):
        solution1 = i
        break 
print(solution1)

#part2 
for (i, char) in enumerate(input[13:], start = 13):
    s = set(input[i-14:i])
    if(len(s) >= 14):
        solution2 = i
        break 
print(solution2)


