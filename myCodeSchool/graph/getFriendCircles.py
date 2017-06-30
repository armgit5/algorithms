# https://www.youtube.com/watch?v=1XuCGYE56T0&index=1&list=PLamzFoFxwoNjmE08l8lNzkl-Sxy9B1fir

friends = [[1,1,0,0],
           [1,1,1,0],
           [0,1,1,0],
           [0,0,0,1]]

def findFriends(friends, visited, id):

    for i in range(len(friends)):
        if visited[i] == False and friends[id][i] == 1:
            visited[i] = True
            findFriends(friends, visited, i)

def getFriendCircles(friends):
    if len(friends) < 1:
        return 0

    noOfCircles = 0
    visited = [False] * len(friends)

    for i in range(len(friends)):
        if visited[i] == False:
            noOfCircles += 1
            visited[i] = True
            findFriends(friends, visited, i)

    return noOfCircles


print(getFriendCircles(friends))