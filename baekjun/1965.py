n = int(input())
boxes = list(map(int, input().split()))

cnt = [1] * len(boxes)

# 나의 최대 상자 갯수를 파악하는 배열을 만들고
# 반복문을 통해 나보다 상자 크기는 작은 것에 +1 을 한후 가장 큰 값을 찾기

for i in range(1, len(boxes)):
    for j in range(i):
        if boxes[j] < boxes[i]:
            cnt[i] = max(cnt[i], cnt[j]+1)

print(max(cnt))