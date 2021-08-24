lottos = input().split()
zuhees = input().split()

cnt = 0
for zuhee in zuhees:
    for i in range(6):
        if lottos[i] == zuhee:
            cnt += 1
            break

if cnt == 6:
    print('1')
elif cnt == 5:
    for zuhee in zuhees:
        if zuhee == lottos[6]:
            print('2')
            break
    else:
        print('3')
elif cnt == 4:
    print('4')
elif cnt == 3:
    print('5')
else:
    print('0')