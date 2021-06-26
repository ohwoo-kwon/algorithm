x, y, w, h = map(int, input().split())

lengths = [x, y, w-x, h-y]

min_len = x
for length in lengths:
    if length < min_len:
        min_len = length
print(min_len)