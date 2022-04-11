N, L = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

for h in heights:
    if L < h:
        break
    L += 1

print(L)