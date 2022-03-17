N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(input()))

hap = 0
result = ""
for i in range(M):
    A, C, G, T = 0, 0, 0, 0
    for j in range(N):
        temp = arr[j][i]
        if temp == "T": T += 1
        elif temp == "A": A += 1
        elif temp == "G": G += 1
        else: C += 1

    if max(A, C, G, T) == A:
        result += "A"
        hap += C + G + T
    elif max(A, C, G, T) == C:
        result += "C"
        hap += A + G + T
    elif max(A, C, G, T) == G:
        result += "G"
        hap += C + A + T
    else:
        result += "T"
        hap += C + A + G
print(result)
print(hap)