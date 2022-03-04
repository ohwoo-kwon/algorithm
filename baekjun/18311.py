N, K = map(int, input().split())
distance_list = list(map(int, input().split()))

total_distance = [distance_list[0]]

for i in range(1, N):
    total_distance.append(total_distance[i-1] + distance_list[i])

for i in range(N-1, -1, -1):
    total_distance.append(distance_list[i] + total_distance[-1])

for idx in range(len(total_distance)):
    if total_distance[idx] > K:
        if idx + 1 <= N:
            print(idx + 1)
        else:
            print(2 * N - idx)
        break
