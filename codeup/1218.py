a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a + b > c:
    if a == b == c:
        print('정삼각형')
    elif a == b or b == c:
        print('이등변삼각형')
    elif a ** 2 + b ** 2 == c ** 2:
        print('직각삼각형')
    else:
        print('삼각형')
else:
    print('삼각형아님')