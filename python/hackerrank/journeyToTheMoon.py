# https://www.hackerrank.com/challenges/journey-to-the-moon/problem


def journeyToMoon(n, astronaut):
    asArr = [set() for i in range(n)]
    visited = [False] * n

    # Make edges
    for a in astronaut:
        asArr[a[0]].add(a[1])
        asArr[a[1]].add(a[0])

    # DFS to find all connected astronaut
    asGroup = []
    for i in range(n):
        asSet = set()
        if visited[i] != True:
            q = [i]
            asSet.add(i)
            visited[i] = True

            while len(q) > 0:
                p = q.pop()
                for v in asArr[p]:
                    if visited[v] != True:
                        q.append(v)
                        asSet.add(v)
                        visited[v] = True

            asGroup.append(asSet)

    # print('as group ', asGroup) # ex [{0, 1, 4}, {2, 3}] or [{0, 2}, {1}, {3}]

    sum = 0
    result = 0
    for country in asGroup:
        result += sum * len(country)
        sum += len(country)
    print(result)

def input():
    return next(f)

with open('journeyToTheMoon2.txt') as f:
    np = input().split()
    n = int(np[0])

    p = int(np[1])

    # print(n, p)

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    # print(n, astronaut)
    journeyToMoon(n, astronaut)
