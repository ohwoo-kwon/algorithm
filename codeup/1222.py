time, score1, score2 = input().split()
time = int(time)
score1 = int(score1)
score2 = int(score2)
goal = 0

for i in range(time, 90, 5):
    goal += 1

if score1 + goal > score2:
    print('win')
elif score1 + goal == score2:
    print('same')
else:
    print('lose')