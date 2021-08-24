N = int(input())

length = list(map(int, input().split()))
money = list(map(int, input().split()))

cheap = 0
i = 0
kilo = 0
result = 0
while i < N-1:
    # 더 싼 가격이 있을 때 까지 찾는다
    if money[cheap] <= money[i]:
        # 계속해서 킬로 수를 더하여 준다
        kilo += length[i]
        i += 1
    else:
        result += kilo * money[cheap]
        cheap = i
        kilo = 0
result += kilo * money[cheap]

print(result)