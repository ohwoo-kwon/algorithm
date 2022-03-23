while True:
    n = int(input())
    if n == 0: break
    words = []
    for _ in range(n):
        word = input()
        words.append((word.lower(), word))

    words.sort()
    print(words[0][1])