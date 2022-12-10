with open("inputs/day08.txt", "r") as f:
    input = [[int(x) for x in line] for line in f.read().split("\n")]
    input_cols = list(zip(*input))

#part1
sol1 = 0
for (i, trees) in enumerate(input):
    for (j, tree) in enumerate(trees):
        if  tree > max(input[i][0:j], default= -1 ) or \
            tree > max(input[i][j+1:], default= -1 ) or \
            tree > max(input_cols[j][0:i], default= -1 ) or\
            tree > max(input_cols[j][i+1:], default = -1):
            sol1 += 1
print("part1: ", sol1)

#part2
def countTrees(tree: int, trees: list[int]) -> int: 
    if not trees:
        return 0
    cnt = 0
    for x in trees:
        cnt += 1
        if x >= tree:
            break
    return cnt

sol2 = 0
for (i, trees) in enumerate(input):
    for (j, tree) in enumerate(trees):
        r = countTrees(tree, input[i][j+1:])
        l = countTrees(tree, input[i][0:j][::-1])
        u = countTrees(tree, input_cols[j][i+1:])
        d = countTrees(tree, input_cols[j][0:i][::-1])
        s = l * r * u * d 
        if s > sol2:
            sol2 = s 
print("part2: ", sol2)

