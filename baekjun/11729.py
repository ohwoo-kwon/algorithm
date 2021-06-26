def Build(N, start, mid, end):
    if N == 1:
        print(start, end)
    else:
        Build(N-1, start, end, mid)
        print(start, end)
        Build(N-1, mid, start, end)

N = int(input())
hanoi = 0
for _ in range(N):
    hanoi = 2 * hanoi + 1
print(hanoi)
Build(N, 1, 2, 3)