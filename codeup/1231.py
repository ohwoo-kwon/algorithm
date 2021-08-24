cal = input()
sik = ['+', '-', '*', '/']

for i in sik:
    if cal.count(i):
        if i == '+':
            print(int(cal[:cal.index(i)]) + int(cal[cal.index(i)+1:]))
            break
        elif i == '-':
            print(int(cal[:cal.index(i)]) - int(cal[cal.index(i)+1:]))
            break
        elif i == '*':
            print(int(cal[:cal.index(i)]) * int(cal[cal.index(i)+1:]))
            break
        else:
            div = round(int(cal[:cal.index(i)]) / int(cal[cal.index(i)+1:]), 2)
            print(div)
            break