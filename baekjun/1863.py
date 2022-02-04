n = int(input())

stack = []
result = 0
for i in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        result += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    if y != 0:
        stack.append(y)

result += len(stack)

print(result)