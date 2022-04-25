from datetime import datetime, timedelta


inputs = open("input.txt")
result = open("output.txt", "w")
N = int(inputs.readline())

for i in range(0, N, 1):
    arr = list(inputs.readline().replace("[", "").replace("]", "").split(","))
    arr = [int(x) for x in arr]
    indx = profit = j = h = 0
    buy = arr[0]
    for price in arr:
        j += 1
        if (price - buy) > profit:
            profit = price - buy
            indx = j

        if price < buy:
            buy = price

    time = datetime(2022, 1, 1, 9, 30, 0)
    time += timedelta(minutes=indx * 10)
    h = time.hour % 12 if time.hour > 12 else time.hour
    minute = time.minute

    if minute == 0:
        minute = "00"

    result.write(f"[{profit},{h}.{minute}]" + "\n")
