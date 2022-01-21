def using_hand(i, N):
    if i != N-1:
        for idx in range(8):
            if not used[i][idx] and not used[i+1][idx]:
                return idx
    else:
        for idx in range(8):
            if not used[i][idx] and not used[0][idx]:
                return idx

N = int(input())
result = [1]
used = [[False] * 8 for _ in range(N)]
used[0][0] = True
used[1][0] = True

for i in range(1, N):
    hand = using_hand(i, N)
    if i != N-1:
        used[i][hand] = True
        used[i+1][hand] = True
    else:
        used[i][hand] = True
        used[0][hand] = True
    result.append(hand+1)

print(*result)