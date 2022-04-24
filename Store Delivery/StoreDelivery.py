inputs = open("input.txt")
N = int(inputs.readline())
result = open("output.txt", "w")


def GetList():
    arr = list(inputs.readline().replace("[", "").replace("]", "").split(","))
    arr = [int(x) for x in arr]
    return arr


for i in range(0, N, 1):
    TakeOutOrder = GetList()
    DineInOrder = GetList()
    ServedOrder = GetList()

    temp1 = temp2 = 0
    check = 1
    for j in range(0, len(ServedOrder), 1):
        if temp1 < len(TakeOutOrder) and TakeOutOrder[temp1] == ServedOrder[j]:
            temp1 += 1
        elif temp2 < len(DineInOrder) and DineInOrder[temp2] == ServedOrder[j]:
            temp2 += 1
        else:
            check = 0
            break
    if check == 1:
        result.write("Valid\n")
    else:
        result.write("Invalid\n")
