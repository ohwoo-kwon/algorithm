def check_room_num(room_num):
    nums = [0] * 10
    while room_num > 0:
        num = room_num % 10
        room_num = room_num // 10
        nums[num] += 1
        if nums[num] > 1:
            return False
    return True

while True:
    try:
        N, M = map(int, input().split())
        result = 0

        for i in range(N, M+1):
            if check_room_num(i):
                result += 1

        print(result)
    except:
        break