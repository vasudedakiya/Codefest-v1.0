from itertools import permutations

inputs = open("input.txt")
N = int(inputs.readline())
result = open("output.txt", "w")
ans = []

for i in range(0, N, 1):
    temp = int(inputs.readline())
    tower = [str(j + 1) for j in range(temp)]
    per = sorted(permutations(tower), reverse=True)

    for p in per:
        ans.append("[" + ",".join(p) + "]")
    result.write("".join(ans) + "\n")
