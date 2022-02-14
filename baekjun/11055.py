N = int(input())
A = list(map(int, input().split()))
cnt_list = [x for x in A]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            cnt_list[i] = max(cnt_list[i], cnt_list[j] + A[i])

print(max(cnt_list))