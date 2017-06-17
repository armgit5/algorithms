unsorted = [2, 4, 6, 8, 3]


def selectionSort(a):

    for i in range(len(a)):
        iMin = i
        for j in range(i, len(a)):
            if a[j] < a[iMin]:
                iMin = j
        temp = a[i]
        a[i] = a[iMin]
        a[iMin] = temp
    return a

print selectionSort(unsorted)