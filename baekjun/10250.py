for t in range(1, int(input()) + 1):
    H, W, N = map(int, input().split())

    if N % H:
        height = N % H
        ho = N // H + 1
    else:
        height = H
        ho = N // H

    print(height * 100 + ho)