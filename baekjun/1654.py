K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end: # start 가 end 보다 커지면 멈춘다
    cnt = 0 # 자른 랜선의 갯수
    mid = (start + end) // 2
    for line in lines:
        cnt += line // mid # 현재 길이로 만들 수 있는 랜선의 갯수

    if cnt < N: # 갯수가 적으면 end 값을 mid -1 로
        end = mid - 1
    else: # 갯수가 많으면 start 값을 mid + 1 로
        start = mid + 1

print(end) # 최종 결과값 end 출력