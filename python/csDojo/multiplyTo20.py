# https://www.youtube.com/watch?v=lD-LuK_VGZI&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev

arr = [1,4,1,6,5,40,-1]

def mulTo20(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        b = int(20 / i)
        if b in dic:
            return i, b

print(mulTo20(arr))


