
memo = {}
times = 2



def fibNoMem(n):
    global times
    times += 1

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

def fib(n):
    global times
    times += 1

    if n <= 1:
        return n
    if n in memo:
        return memo[n]


    result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result

def fibOneSpace(n):

    global times
    times += 1

    if n <= 1:
        return n

    prev_prev = 0
    prev = 1
    current = 0

    for _ in range(n - 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

times = 0
print(fibNoMem(11), times)
times = 0
print(fib(11), times)
times = 0
print(fibOneSpace(11), times)