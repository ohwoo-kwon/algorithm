n = int(input())
numbers = map(int, input().split())

total = 0
for number in numbers:
    if number % 5 == 0:
        total += number

print(total)