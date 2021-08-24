N = int(input())

numbers = [0] * 10000001
numbers[1] = 1
numbers[2] = 2
for i in range(3, N+1):
    numbers[i] = (numbers[i-1]+numbers[i-2])%15746
print(numbers[N])