a = list(input().split())

cal = []

for b in range(2):
    if a[b] == '1':
        cal.append(400)
    elif a[b] == '2':
        cal.append(340)
    elif a[b] == '3':
        cal.append(170)
    elif a[b] == '4':
        cal.append(100)
    elif a[b] == '5':
        cal.append(70)

if sum(cal) > 500:
    print('angry')
else:
    print('no angry')