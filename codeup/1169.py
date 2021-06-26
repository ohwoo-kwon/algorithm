a = int(input())

if a > 13:
    year = 112 - a + 1
    print(str(year) + ' 1')
else:
    year = 12 - a + 1
    print(str(year) + ' 3')