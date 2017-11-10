# https://codility.com/c/run/demo58PUSG-R6A
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.


def solution(A):
    # write your code in Python 2.7
    map = {}
    smallest = 1000
    for i in A:
        map[i] = 1

    for i in range(len(A)):
        next = A[i] + 1
        if next not in map:
            if next < smallest:
                smallest = next
    if smallest <= 0:
        return 1
    else:
        return smallest



s = solution([1 ,3 ,6 ,4 ,1 ,2])
print(s)
print("")
s = solution([1, 2, 3])
print(s)
print("")
s = solution([-1, -3])
print(s)

