str_a = input()
str_b = input()

A = len(str_a)
B = len(str_b)
result = 0

arr = [[0 for _ in range(B+1)] for _ in range(A+1)]

for r in range(A):
    for c in range(B):
        if str_a[r] == str_b[c]:
            arr[r][c] = arr[r-1][c-1] + 1
        else:
            arr[r][c] = max(arr[r-1][c], arr[r][c-1])

print(arr[A-1][B-1])