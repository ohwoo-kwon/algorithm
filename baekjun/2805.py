N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2 # 절단기의 높이
    h = 0 # 가져갈 나무의 높이
    for tree in trees:
        if tree > mid:
            h += tree - mid

    if h < M: # 높이가 모자라다면
        end = mid - 1 # 절단기의 높이를 낮추고
    else: # 높이가 충분하다면
        start = mid + 1 # 절단기의 높이를 높여본다.

print(end)