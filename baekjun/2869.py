import math

a, b, v = map(int, input().split())

x = math.ceil((v - a) / (a - b)) + 1
print(x)