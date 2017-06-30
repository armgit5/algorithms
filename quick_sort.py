# unsorted = [2, 4, 6, 8, 3]
unsorted = [2,1,3,6,8,5,7,4]
unsorted = list(map(int, ['31415926535897932384626433832795', '1', '3', '10', '3', '5']))


def partition(a, start, end):
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1

    a[pIndex], a[end] = a[end], a[pIndex]

    return pIndex


def quickSort(a, start, end):

    if start < end:
        pIndex = partition(a, start, end)
        quickSort(a, start, pIndex - 1)
        quickSort(a, pIndex + 1, end)




quickSort(unsorted, 0, len(unsorted) - 1)
print('\n'.join(map(str, unsorted)))
