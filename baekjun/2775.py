# def ceo(n, k):
#     if n == 0:
#         return k
#     elif k == 1:
#         return 1
#     else:
#         return ceo(n,k-1) + ceo(n-1, k)
#
# for t in range(1, int(input())+1):
#     n = int(input())
#     k = int(input())
#     print(ceo(n, k))
# 시간초과 나옴

for t in range(1, int(input())+1):
    n = int(input())
    k = int(input())
    floor = [x for x in range(1, k+1)]
    for _ in range(n):
        for i in range(1, k):
            floor[i] += floor[i-1]
    print(floor[-1])