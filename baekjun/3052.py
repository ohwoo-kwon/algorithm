div_nums = []
cnt = 0
for i in range(10):
    a = int(input())
    div_nums += [a % 42]

for i in range(42):
    if div_nums.count(i):
        cnt +=1
print(cnt)