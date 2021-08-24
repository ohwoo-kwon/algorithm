height, weight = input().split()

height = float(height)
weight = float(weight)

n_weight = (height - 100) * 0.9
over = (weight - n_weight)*100 / n_weight

if over > 20:
    print('비만')
elif over > 10:
    print('과체중')
else:
    print('정상')