N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    result = 0
    if number == 1:
        continue
    for i in range(2, number):
        if number % i:
            continue
        else:
            result += 1
    if result == 0:
        cnt += 1

print(cnt)