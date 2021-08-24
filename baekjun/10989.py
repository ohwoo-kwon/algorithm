N = int(input())

C = [0 for _ in range(10000+1)]

for _ in range(N):
    C[int(input())] += 1

for i in range(10000+1):
    for _ in range(C[i]):
        print(i)