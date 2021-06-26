remain_time, score = input().split()

remain_time = int(remain_time)
score = int(score)
t_list = []

for i in range(remain_time, 90, 5):
    t_list.append(i)

print(score + len(t_list))