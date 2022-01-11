N = int(input())
colors = input()
now = colors[0]
blue = 0
red = 0

if now == "R":
    red += 1
else: blue += 1

for color in colors:
    if color != now:
        if color == "B":
            blue += 1
            now = "B"
        else:
            red += 1
            now = "R"

print(1 + min(blue, red))