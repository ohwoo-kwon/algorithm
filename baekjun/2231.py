N = int(input())

for i in range(N):
    cnt = i
    number = i
    while i != 0:
        cnt += i % 10
        i //= 10
    if cnt == N:
        print(number)
        break
else:
    print(0)