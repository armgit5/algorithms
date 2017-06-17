
unsorted = [2, 4, 6, 8, 3]


def bubbleSort(a):

    for k in range(1, len(a) - 1):
        flag = 0
        for i in range(len(a) - k - 1):
            if a[i] > a[i + 1]:
                tmp = a[i + 1]
                a[i + 1] = a[i]
                a[i] = tmp
                flag = 1
        if flag == 0:
            return a;
    return a


print bubbleSort(unsorted)