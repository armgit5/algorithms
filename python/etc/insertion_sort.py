ar = [2, 4, 6, 8, 3]
ar = [1,4,3,5,6,2]
# ar = [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23]
# ar = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

def insertionSort(a):
    # key = ar[-1]
    # key_pos = len(ar) - 1
    # i = len(ar) - 2
    # done = False
    # while  i >= 0 and done == False:
    #
    #     if ar[i] > key:
    #         ar[i+1] = ar[i]
    #         print ' '.join(map(str, ar))
    #     elif ar[i] < key:
    #         ar[i+1] = key
    #         print ' '.join(map(str, ar))
    #         done = True
    #     if i == 0 and done == False:
    #         ar[i] = key
    #         print ' '.join(map(str, ar))
    #     i -= 1

    for i in range(len(a)):
        value = a[i]
        hole = i
        while hole > 0 and a[hole - 1] > value:

            a[hole] = a[hole - 1]
            hole = hole - 1

        a[hole] = value
        if i >= 1:
            print(' '.join(map(str, a)))

print(insertionSort(ar))

