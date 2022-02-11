# 숫자를 입력 받고 숫자의 길이 체크
# 0 과 길이 n-1 비교
# 1 과 길이 n-2 비교
# n//2 까지 반복

while True:
    num = input()
    if num == "0":
        break
    n = len(num)
    for i in range(n//2):
        if num[i] != num[n-1-i]:
            print("no")
            break
    else:
        print("yes")
