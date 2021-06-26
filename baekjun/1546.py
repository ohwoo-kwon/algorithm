N = int(input())

scores = list(map(int, input().split()))
c_scores = []

max_scores = max(scores)

for score in scores:
    score = score / max_scores * 100
    c_scores += [score]

print(sum(c_scores) / N)