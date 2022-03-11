for _ in range(int(input())):
    first_num, second_num = input().split()
    first_num = list(first_num)
    second_num = list(second_num)

    cnt_one_in_first_num = 0
    cnt_one_in_second_num = 0
    for i in range(len(first_num)):
        if first_num[i] == "1":
            cnt_one_in_first_num += 1
        if second_num[i] == "1":
            cnt_one_in_second_num += 1

    result = abs(cnt_one_in_first_num - cnt_one_in_second_num)
    temp = result
    for i in range(len(first_num)):
        if temp == 0:
            break
        if first_num[i] != second_num[i]:
            first_num[i] = second_num[i]
            temp -= 1

    diff_cnt = 0
    for i in range(len(first_num)):
        if first_num[i] != second_num[i]:
            diff_cnt += 1

    result += diff_cnt // 2
    print(result)