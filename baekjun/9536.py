for _ in range(int(input())):
    voices = input().split()
    temp = input()
    while temp != "what does the fox say?":
        word = temp.split()[2]
        for i in range(voices.count(word)):
            voices.remove(word)
        temp = input()
    print(*voices)