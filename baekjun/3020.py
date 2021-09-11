N, H = map(int, input().split())

top = [0] * (H+1) # 종유석
bottom = [0] * (H+1) # 석순

min_cnt = N # 파괴해야 할 장애물의 최솟값
result = 0 # 최솟값 구간의 수

for i in range(N): # 입력 값을 받으며 해당 높이의 종유석과 석순의 갯수를 입력
    if i % 2: # 종유석
        top[int(input())] += 1
    else: # 석순
        bottom[int(input())] += 1

for i in range(H-1, 0, -1): # 자기보다 높은 석순 혹은 종유석에는 무조건 부딪히므로 자신의 높이보다 높은 모든 석순 혹은 종유석을 더해준다
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]

for i in range(1, H+1):
    cur = bottom[i] + top[H-i+1] # 현재 벌레가 부딪힐 장애물 갯수
    if min_cnt > cur:
        min_cnt = cur
        result = 1
    elif min_cnt == cur:
        result += 1

print(min_cnt, result)