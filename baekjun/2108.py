import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
numbers = []
cnt = 0
for _ in range(N):
    n = int(input())
    numbers += [n]
    cnt += n

numbers.sort()

a = int(round(cnt/N, 0))
b = numbers[N//2]

common = Counter(numbers).most_common()
if N > 1:
    if common[0][1] == common[1][1]:
        c = common[1][0]
    else:
        c = common[0][0]
else: c = numbers[0]

d = numbers[-1] - numbers[0]

print(a)
print(b)
print(c)
print(d)