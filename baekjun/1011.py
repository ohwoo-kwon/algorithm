# def Space(N):
#     if N == 1:
#         arr = [1]
#         return arr
#     elif N == 2:
#         arr = [1,1]
#         return arr
#     elif N == 3:
#         arr = [1,1,1]
#         return arr
#     else:
#         arr = Space(N-1)
#         i = len(arr) // 2
#         while i < len(arr)-1:
#             arr[i] += 1
#             if arr[i] - arr[i-1] < -1 or arr[i] - arr[i-1] > 1 or arr[i] - arr[i+1] < -1 or arr[i] - arr[i+1] > 1:
#                 arr[i] -= 1
#                 i += 1
#                 continue
#             break
#         if i == len(arr) - 1: arr.append(1)
#         return arr




for t in range(1, int(input())+1):
    x, y = map(int, input().split())
    N = y - x
    i = 0
    j = 1
    cnt = 0
    while i < N:
        if cnt % 2:
            i += j
            j += 1
            cnt += 1
        else:
            i += j
            cnt += 1
    print(cnt)