strings = input()

time = 0
for string in strings:
    if string in 'ABC':
        time += 3
    elif string in 'DEF':
        time += 4
    elif string in 'GHI':
        time += 5
    elif string in 'JKL':
        time += 6
    elif string in 'MNO':
        time += 7
    elif string in 'PQRS':
        time += 8
    elif string in 'TUV':
        time += 9
    else:
        time += 10
print(time)