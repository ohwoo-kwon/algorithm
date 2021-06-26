C = int(input())

for c in range(C):
    scores = list(map(int, input().split()))

    N = scores[0]
    scores.pop(0)

    average = sum(scores) / N

    cnt = 0
    for score in scores:
        if score > average:
            cnt += 1

    percent = cnt / N * 100
    print(f'{percent:.3f}%')