numbers = []
for i in range(9):
    numbers += [int(input())]
print(max(numbers))
print(numbers.index(max(numbers))+1)