problem = input().split('-')

for i in range(len(problem)):
    pro = list(map(int, problem[i].split('+')))
    result = 0
    for num in pro:
        result += num
    problem[i] = result
result = problem[0]
for i in range(1, len(problem)):
    result -= problem[i]

print(result)