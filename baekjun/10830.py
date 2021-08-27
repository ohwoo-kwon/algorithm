def multiply(arr1, arr2):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j] %= 1000
    return result

def power(A, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif b % 2: # 홀수이면
        return multiply(power(multiply(A, A), b//2), A)
    else:
        return power(multiply(A, A), b//2)


N, B = map(int, input().split())
A = []

for _ in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

answer = power(A, B)

for line in answer:
    for num in line:
        print(num, end=" ")
    print()