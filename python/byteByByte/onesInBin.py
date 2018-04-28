# https://www.youtube.com/watch?v=8iWIpkFgZ64&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=4
# Find numbers of ones in binary

# 6 = 0b110
# 6 & 1 = 0
# 6 >> 1 = 0b11 = 3
# 3 & 1 = 1

def ones(x):
    sum = 0
    while x > 0:
        sum += x & 1
        x >>= 1
    return sum

print(ones(7))
print(ones(6))
print(ones(5))
print(ones(4))
print(ones(3))
print(ones(2))