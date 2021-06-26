M = int(input())
N = int(input())

count = 0
numbers = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += i
        numbers += [i]
if count:
    print(count, numbers[0])
else:
    print(-1)