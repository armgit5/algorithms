# https://github.com/rkm-elgo/INOI-2015/blob/master/inoi2005-qpaper.pdf
# http://elgoacademy.org/frog-jumping-nptel-week-2-programming-assignment/

import sys

n, s, t, r_0, g, seed, p = [9, 0, 2, 1, 3, 4, 7]
# n, s, t, r_0, g, seed, p = [10000000, 2288596, 8380906, 5121, 69, 3662, 5585]

min_jump = sys.maxint

def circularWalk(n, s, t, r_0, g, seed, p):
    R = []
    current_r = r_0
    queue = []

    if s == t:
        return 0

    for i in xrange(n):
        R.append(current_r)
        current_r = (current_r * g + seed) % p

    def walk_right(s, step, dist):
        global min_jump
        for i in range(1, step+1):
            x = (s+i) % n
            if x == t:
                if dist < min_jump:
                    min_jump = dist


    def walk_left(s, step, dist):
        global min_jump
        for i in range(1, step+1):
            x = (s-i) % n
            if x == t:
                if dist < min_jump:
                    min_jump = dist

    queue.append((s,1))

    def find_min_jump():
        global min_jump

        while len(queue) != 0:
            x = queue.pop(0)
            s = x[0]
            dist = x[1]

            walk_left(s, R[s], dist)
            walk_right(s, R[s], dist)

            for i in range(1, R[s]+1):
                if R[(s-i) % n] > R[s]:
                    queue.append(((s-i) % n, dist+1))

            for i in range(1, R[s]+1):
                if R[(s+i) % n] > R[s]:
                    queue.append(((s+i) % n, dist+1))

    find_min_jump()
    return min_jump

def circularWalk2(n, s, t, r_0, g, seed, p):
    a = [0] * 10000005
    a[0] = r_0
    a.append(r_0)
    b = [0] * 10000005
    wal = [0] * 10000005


    for i in range(1, n):
        a[i] = (a[i-1] * g + seed) % p

    for i in range(n):
        b[i] = a[(i+s) % n]


    t = (t - s + n) % n
    l = 0
    r = 0

    for i in range(n):
        if t <= r or t >= n + l:
            return i
        pl = l
        pr = r

        j = pl
        while j < 0:
            if wal[j+n]: break
            else:
                r = max(r, j + b[j + n])
                l = min(l, j - b[j + n])
                wal[j + n] = 1
            j += 1
        j = pr
        while j >= 0:
            if wal[j]: break
            else:
                r = max(r, j + b[j])
                l = min(l, j - b[j])
                wal[j] = 1
            j -= 1
        # print wal[:100]
    return -1


def circularWalk3(n, s, t, r_0, g, seed, p):
    if s == t:
        return 0
    R = [r_0]
    for i in range(1, n):
        R.append((R[i - 1] * g + seed) % p)

    visited = [-1 for i in range(n)]

    l, r = s, s
    pl, pr = l + 1, r - 1
    hop = 0

    while True:
        nl, nr = l, r
        i = pl
        while i != l:
            i = i - 1
            if visited[i % n] == -1:
                visited[i % n] = hop
                if i - R[i % n] < nl:
                    nl = i - R[i % n]
                if i + R[i % n] > nr:
                    nr = i + R[i % n]

        i = pr
        while i != r:
            i = i + 1
            if visited[i % n] == -1:
                visited[i % n] = hop
                if i - R[i % n] < nl:
                    nl = i - R[i % n]
                if i + R[i % n] > nr:
                    nr = i + R[i % n]

        hop += 1
        if nl == l and nr == r:
            break
        l, r, pl, pr = nl, nr, l, r

    return visited[t]

def solve(N, S, T, R0, G, SEED, P):
    R = [R0]
    for _ in xrange(N - 1):
        R.append((R[-1] * G + SEED) % P)

    def get(x):
        return R[x % N]

    oldstart, oldend = S, S
    start, end = S, S
    ans = 0
    while not (start <= T <= end or start <= T - N <= end or start <= T + N <= end):
        newstart = start
        newend = end
        for x in xrange(start, oldstart + 1):
            j = get(x)
            newstart = min(newstart, x - j)
            newend = max(newend, x + j)

        for x in xrange(oldend, end + 1):
            j = get(x)
            newstart = min(newstart, x - j)
            newend = max(newend, x + j)
        if newstart == oldstart and newend == oldend: return -1
        oldstart, oldend = start, end
        start, end = newstart, newend
        ans += 1
    return ans


print circularWalk3(n, s, t, r_0, g, seed, p)

