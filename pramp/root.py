# https://www.pramp.com/question/jKoA5GAVy9Sr9jGBjzN4

def root(x, n):
    if x == 0:
        return 0
    low = 0
    high = x
    mid = (low + high) / 2

    while mid - low >= 0.001:
        if mid ** n > x:
            high = mid
        elif mid ** n < x:
            low = mid
        else:
            break
        mid = (high + low) / 2
    return mid

print(root(9.0,2))
print(root(7.0,3))