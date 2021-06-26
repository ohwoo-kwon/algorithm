def self_num(b):
    count = b
    for i in range(len(str(b))):
        count += b % 10
        b //= 10
    return count

numbers = []
for i in range(1, 10000):
    numbers += [self_num(i)]

for i in range(1, 10000):
    if numbers.count(i) == 0:
        print(i)