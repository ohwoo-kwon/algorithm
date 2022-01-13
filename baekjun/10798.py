arr = []
max_len = 0

for _ in range(5):
    temp = list(input())
    arr.append(temp)
    max_len = max(max_len, len(temp))

for c in range(max_len):
    for r in range(5):
        if len(arr[r]) <= c:
            continue
        print(arr[r][c], end="")