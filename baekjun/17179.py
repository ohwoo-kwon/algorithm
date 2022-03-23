def is_ok(min_v):
    left = 0
    cnt = 0
    for right in cut_points:
        if right - left >= min_v:
            cnt += 1
            left = right
    if cnt > cut_cnt:
        return True
    return False



N, M, L = map(int, input().split())
cut_points = [int(input()) for _ in range(M)] + [L]
cut_cnts = [int(input()) for _ in range(N)]
for cut_cnt in cut_cnts:
    left = 1
    right = 4000000
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if mid > L:
            right = mid -1
            continue
        if is_ok(mid):
            left = mid + 1
            result = max(mid, result)
        else:
            right = mid - 1
    print(result)