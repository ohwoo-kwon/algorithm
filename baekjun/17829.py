def find_second(lst):
    lst.sort()
    return lst[2]

N = int(input())

arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

while N != 1:
    result = []
    for i in range(N//2):
        for j in range(N//2):
            r1 = 2*i
            r2 = 2*i + 1
            c1 = 2*j
            c2 = 2*j + 1

            temp_list = [(arr[r1][c1], r1, c1), (arr[r1][c2], r1, c2), (arr[r2][c1], r2, c1), (arr[r2][c2], r2, c2)]
            value, r, c = find_second(temp_list)
            if j == 0:
                result.append([value])
            else:
                result[i].append(value)
    arr = result
    N //= 2
print(result[0][0])