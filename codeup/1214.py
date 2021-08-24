year, month = input().split()
year = int(year)
month = int(month)
yoon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
no_yoon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 400 == 0:
    print(yoon[month])
elif (year %  4 == 0) & (year % 100 != 0):
    print(yoon[month])
else:
    print(no_yoon[month])