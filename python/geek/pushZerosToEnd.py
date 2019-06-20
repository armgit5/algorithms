# https://www.youtube.com/watch?v=0jXTju134Hw&index=24&list=PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE

arr = [1,9,8,4,0,0,2,7,0,6,0,9]

def pushZerosToEnd(arr):
    count = 0

    # loop all element, skip 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # the remaining elements should be 0
    while count < len(arr):
        arr[count] = 0
        count += 1


pushZerosToEnd(arr)
print(arr)