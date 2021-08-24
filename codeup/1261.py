numbers = input().split()

for number in numbers:
    if int(number) % 5 == 0:
        print(number)
        break
else:
    print('0')