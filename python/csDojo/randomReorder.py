# https://www.youtube.com/watch?v=CoI4S7z1E1Y&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=9
from math import floor
import random

arr = [1, 0, 3, 9, 2]

def reorder(arr):
    for i in range(len(arr)-1, -1, -1):
        pick = floor(random.randrange(0, i+1))
        temp = arr[i]
        arr[i] = arr[pick]
        arr[pick] = temp

reorder(arr)
print(arr)