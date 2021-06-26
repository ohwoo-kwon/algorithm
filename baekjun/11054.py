N = int(input())
num_list = list(map(int, input().split()))

left = [0] * N
right = [0] * N
result = [0] * N

'''
1 5 2 1 4 3 4 5 2 1
0 1 1 0 3 3 4 5 2 0
'''

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j] and left[i] < left[j]:
            left[i] = left[j]
    left[i] += 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if num_list[i] > num_list[j] and right[i] < right[j]:
            right[i] = right[j]
    right[i] += 1

for i in range(N):
    result[i] = left[i] + right[i] - 1

print(max(result))
