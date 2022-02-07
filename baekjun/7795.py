def binary_search(num):
    s = 0
    e = len(b_list) - 1
    res = -1
    while s <= e:
        mid = (s+e) // 2
        if num <= b_list[mid]:
            e = mid - 1
        else:
            s = mid + 1
            res = mid
    return res

for _ in range(int(input())):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = sorted(list(map(int, input().split())))
    cnt = 0
    for a in a_list:
        result = binary_search(a) + 1
        cnt += result
    print(cnt)