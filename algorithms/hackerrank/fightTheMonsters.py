




def raw_input():
    return next(f)

def getMaxMonsters_old(n, hit, t, h):
    # Complete this function
    h.sort()
    zombie_index = 0

    for i in range(t):

        if zombie_index < n:
            h[zombie_index] -= hit
            if h[zombie_index] <= 0:
                zombie_index += 1

    return zombie_index

def getMaxMonsters(n, hit, t, h):
    # Complete this function
    h.sort()
    counter = 0

    for i in range(n):

        time = h[i]/hit + int(h[i]%hit != 0)
        t -= time
        if t >= 0:
            counter += 1
        if t <= 0:
            break

    return counter




with open('fightTheMonsters.txt') as f:
    n, hit, t = raw_input().strip().split(' ')
    n, hit, t = [int(n), int(hit), int(t)]
    h = map(int, raw_input().strip().split(' '))

    result = getMaxMonsters(n, hit, t, h)
    print result

