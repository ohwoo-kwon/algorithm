N, C = map(int, input().split())
houses = []

for _ in range(N):
    houses.append(int(input()))

houses.sort()

def binary_search(start, end):
    while start <= end:
        mid = (start+end)//2
        cur = houses[0]
        cnt = 1

        for i in range(1, N):
            if houses[i] >= cur + mid:
                cnt += 1
                cur = houses[i]

        if cnt >= C:
            global result
            start = mid + 1
            result = mid
        else: end = mid - 1

start = 1
end = houses[-1] - houses[0]
result = 0

binary_search(start, end)
print(result)