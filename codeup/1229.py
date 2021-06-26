h, w = map(float, input().split())

if h >= 160:
    n_w = (h - 100) * 0.9
elif h >= 150:
    n_w = (h - 150) / 2 + 50
else:
    n_w = h - 100

over = (w - n_w) * 100 / n_w

if over <= 10:
    print('정상')
elif over <= 20:
    print('과체중')
else:
    print('비만')