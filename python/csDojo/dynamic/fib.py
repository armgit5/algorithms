
n = 6
memo = [None] * (n+1)

def fib(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
        return 1

    result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    print(memo)
    return result

def fib_bottom_up(n):
    bottom_up = [0] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

print(fib(n, memo))
print(fib_bottom_up(n))