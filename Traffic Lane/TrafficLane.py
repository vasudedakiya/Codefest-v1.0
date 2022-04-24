inputs = open("input.txt")
N = int(inputs.readline())
output = []
temp = {}
for i in range(0, N, 1):
    arr = list(inputs.readline().replace("[", "").replace("]", "").split(","))
    arr = [int(x) for x in arr]
    arr = list(set(arr))
    temp[i] = sum(arr)

temp = dict(sorted(temp.items(), key=lambda item: item[1]))
for key, value in temp.items():
    output.append(key + 1)
    output.append(value)
inputs.close()

result = open("output.txt", "w")
result.write(str(output))
