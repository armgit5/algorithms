

import sys

n = 360
s = "aaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbccccccccccaaaaaaaaaabbbbbbbbbbcccccccccc"
# n = 15
# s = "ccaccbbbaccccca"



def geometricTrick(s):
    # Complete this function

    queue = []
    ans = 0

    def if_b_exceeded():
        b = n

    def find_c(a,b):
        if (b+1)**2 % (a+1) == 0:
            c = ((b + 1) ** 2 / (a + 1)) - 1
            return c
        return -1

    def num_valid(a,b,c):
        if (b + 1) ** 2 == (a + 1) * (c + 1):
            return True
        return False

    def is_abc(i,j,k):
        if s[i] == "a" and s[j] == "b" and s[k] == "c":
            return True
        return False


    for i in range(n):
        for j in range(n):
            c = find_c(i,j)
            if c >= n:
                break
            if c > 0 and c < n:

                if is_abc(i, j, c):
                    ans += 1

    return ans


    # def next_cha():
    #     if len(queue) < 3:
    #         if len(queue) == 0:
    #             return "a"
    #         last_c = queue[-1][0]
    #         next_index = cha_set.index(last_c) + 1
    #         return cha_set[next_index]
    #
    #
    # def is_valid():
    #     global ans
    #     if (queue[1][1]+1) ** 2 == (queue[0][1]+1) * (queue[2][1]+1):
    #         ans += 1
    #         return True
    #     return False


    # while len(queue) <= 3 and i < n:
    #     if s[i] == next_cha():
    #         queue.append((s[i], i))
    #         j = 0
    #         while len(queue) != 0 and j < n:
    #             if s[j] == next_cha():
    #                 queue.append((s[j], j))
    #                 k = 0
    #                 while len(queue) <= 3 and k < n:
    #                     if s[k] == next_cha():
    #                         queue.append((s[k], k))
    #                         if is_valid() == True:
    #                             queue = []
    #                             break
    #                         else:
    #                             queue.pop()
    #                     k += 1
    #                 else:
    #                     queue.pop()
    #             j += 1
    #     i += 1
    # return ans


def squarefree(x):
    free = 1
    xx = x
    for p in primes:
        countp = 0
        while xx % p == 0:
            countp += 1
            xx /= p
        if countp % 2 == 1:
            free *= p
        if xx == 1:
            break
    return free * xx


def firststrategy(word):
    n = len(word)
    bword = set([j for j in xrange(n) if word[j] == 'b'])
    cword = set([k for k in xrange(n) if word[k] == 'c'])
    counter = 0
    for i, v in enumerate(word):
        if word[i] == 'a':
            ip = i + 1
            free = squarefree(ip)
            for t in xrange(n):
                kp = free * (t ** 2)
                k = kp - 1
                if k >= n:
                    break
                if k in cword:
                    jp = int((ip * kp) ** 0.5)
                    j = jp - 1
                    if j in bword:
                        counter += 1
    return counter

result = geometricTrick(s)
print(result)