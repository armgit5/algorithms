# https://www.pramp.com/question/7Lg1WA1nZqfoWgPbgM0M

arr = [8, 10, 2]
# [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

arr2 = [2, 7, 3, 4]
# output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]

def calProductArrayBruteForce(arr):
    prodArr = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i == j:
                continue
            product *= arr[j]
        prodArr.append(product)
    return prodArr

print(calProductArrayBruteForce(arr))
print(calProductArrayBruteForce(arr2))


'''
arr = [8,       10,     2,      7]
left   1        a0      a0a1    a0a1a2
right  a1a2a3   a2a3    1a3     1       
result a1a2a3   aa2a3   a0a1a3 a0a1a2
'''
def calProductArray(arr):
    prodArr = []
    left = [1] * len(arr)
    right = [1] * len(arr)

    for i in range(1,len(arr)):
        left[i] = left[i-1] * arr[i]
        right[len(arr)-i] = right[len(arr)-i-1] * arr[i]

    for i in range(len(arr)):
        prodArr[i] = left[i] * right[i]

    return prodArr

print(calProductArrayBruteForce(arr))
print(calProductArrayBruteForce(arr2))




