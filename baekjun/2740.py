N, M = map(int, input().split())
arr1 = []
arr2 = []
result = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    arr1.append(tmp)

M, K = map(int, input().split())

for _ in range(M):
    tmp = list(map(int, input().split()))
    arr2.append(tmp)

for n in range(N):
    tmp = []
    for k in range(K):
        mul = 0
        for m in range(M):
            mul += arr1[n][m] * arr2[m][k]
        tmp.append(mul)
    result.append(tmp)

for line in result:
    for num in line:
        print(num, end=" ")
    print()
