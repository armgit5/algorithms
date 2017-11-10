with open('test.txt') as f:
    a, b = list(map(int, next(f).split()))

    print(a, b)