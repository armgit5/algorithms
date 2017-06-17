
M = [[2,4,6,8],
     [5,9,12,16],
     [2,11,5,9],
     [3,2,1,8]]

def spiral(M):
    T = 0
    B = len(M)-1
    L = 0
    R = len(M[0])-1
    dir = 0

    while T<=B and L<=R:
        if dir == 0:
            for i in range(R+1):
                a = M[T][i]
                print M[T][i]
            T += 1
        if dir == 1:
            for i in range(T,B+1):
                print M[i][R]
            R -= 1
        if dir == 2:
            for i in range(R,L-1,-1):
                a = M[B][i]
                print M[B][i]
            B -= 1
        if dir == 3:
            for i in range(B,T,-1):
                print M[i][L]
            L += 1
        dir = (dir + 1) % 4

spiral(M)