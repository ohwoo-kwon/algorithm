n = int(input())
# 첫번째 문자 받아서 결과에 저장
# 다음 문자 받아서 결과와 비교하며 다른 부분은 ? 로 전환
result = ""
for i in range(n):
    if i == 0:
        result = input()
    else:
        temp = input()
        for idx in range(len(result)):
            if result[idx] == "?":
                continue
            elif result[idx] != temp[idx]:
                temp_list = list(result)
                temp_list[idx] = "?"
                result = "".join(temp_list)
print(result)