num = input()
result = 0
temp = num

while True:
    if len(temp) == 1:
        temp = "0" + temp

    sum_v = int(temp[0]) + int(temp[1])
    temp = temp[-1] + str(sum_v)[-1]
    result += 1
    if int(temp) == int(num):
        break

print(result)