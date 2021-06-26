N = int(input())

scores = [0] * 301
stairs = [0] * 301
for i in range(N):
    scores[i] = int(input())

stairs[0] = scores[0]
stairs[1] = scores[0] + scores[1]
stairs[2] = max(scores[1]+scores[2], scores[0]+scores[2])
for i in range(3, N):
    stairs[i] = max(stairs[i-3] + scores[i-1] + scores[i], stairs[i-2] + scores[i])

print(stairs[N-1])