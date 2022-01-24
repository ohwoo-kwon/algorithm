money = int(input())
prices = list(map(int, input().split()))

first_have = 0
second_have = 0

# prices 값을 하나씩 빼면서 가능한 만큼 매수
# 현재 주식 수와 남은돈 계산
temp = money
for price in prices:
    if temp // price:
        first_have += temp//price
        temp -= price * (temp//price)
first_result = prices[-1] * first_have + temp

# prices 값을 하나씩 빼면서 가능한 만큼 매수
# 3일 이상
temp = money
up = 0
down = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        up += 1
        down = 0
    elif prices[i] < prices[i-1]:
        down += 1
        up = 0
    else:
        up = 0
        down = 0

    if down >= 3:
        second_have += temp // prices[i]
        temp -= prices[i] * (temp // prices[i])
    elif up >= 3:
        temp += second_have * prices[i]
        second_have = 0
second_result = second_have * prices[-1] + temp

if first_result > second_result:
    print("BNP")
elif first_result < second_result:
    print("TIMING")
else:print("SAMESAME")