array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# O(N^2) -> 상태에 따라 매우 빠름 -> 어느 정도 정렬되어 있을 경우 매우 빠르게 작동