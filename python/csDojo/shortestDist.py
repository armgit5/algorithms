# https://www.youtube.com/watch?v=eaYX0Ee0Kcg&index=3&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev
import math
from csDojo.maxHeapTuple import MaxHeapTuple

points = [(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2)]

def shortestDist(points, n):
    pointWithD = {}
    mHeap = MaxHeapTuple()
    for i in points:
        d = math.sqrt(i[0]**2 + i[1]**2)
        pointWithD[i] = d

    for i in range(3):
        mHeap.push((points[i], pointWithD[points[i]]))

    for p in points[n:len(points)]:
        if pointWithD[p] < mHeap.peek()[1]:
            print(pointWithD[p], mHeap.peek()[1])
            mHeap.pop()
            mHeap.push((p, pointWithD[p]))
    print(str(mHeap.heap[0:len(mHeap.heap)]))



shortestDist(points, 3)