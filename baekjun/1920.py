def binary_search(x): # 이진 탐색
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if x < nums[mid]:
            end = mid - 1
        elif x > nums[mid]:
            start = mid + 1
        else:
            print(1)
            return
    print(0)

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
find_nums = list(map(int, input().split())) # 찾아야 할 수들이 담겨있는 리스트

# num 리스트 오름차순으로 정렬
nums.sort()

for num in find_nums:
    binary_search(num)