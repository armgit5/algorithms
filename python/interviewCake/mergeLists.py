my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists(left, right):
    i = 0
    j = 0
    retList = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            retList.append(left[i])
            i += 1
        else:
            retList.append(right[j])
            j += 1
    retList += left[i:]
    retList += right[j:]
    return retList

print(merge_lists(my_list, alices_list))

