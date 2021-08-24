point_1 = list(map(int, input().split()))
point_2 = list(map(int, input().split()))
point_3 = list(map(int, input().split()))
point_4 = []
if point_1[0] == point_2[0]:
    point_4 += [point_3[0]]
elif point_1[0] == point_3[0]:
    point_4 += [point_2[0]]
else:
    point_4 += [point_1[0]]

if point_1[1] == point_2[1]:
    point_4 += [point_3[1]]
elif point_1[1] == point_3[1]:
    point_4 += [point_2[1]]
else:
    point_4 += [point_1[1]]

print(point_4[0], point_4[1])