T = int(input())

for t in range(T):
    scores = input()
    cnt = 0
    result = 0
    for score in scores:
        if score == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)