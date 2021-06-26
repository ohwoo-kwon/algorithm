X = int(input())

# m = 1
# n = 1
# cnt = 1
# while True:
#     if cnt == X:
#         break
#     if n == 1 and (m+n) % 2:
#         m += 1
#         cnt += 1
#         continue
#     elif m == 1 and (m+n) % 2 == 0:
#         n += 1
#         cnt += 1
#         continue
#     elif (m+n) % 2:
#         m += 1
#         n -= 1
#         cnt += 1
#         continue
#     else:
#         m -= 1
#         n += 1
#         cnt += 1
#         continue
#
# print(f'{m}/{n}')

i = 1
fibo = 1
while X > fibo:
    i += 1
    fibo += i

diff = fibo - X

if i%2:
    m = 1 + diff
    n = i - diff
else:
    m = i - diff
    n = 1 + diff

print(f'{m}/{n}')