# https://www.hackerrank.com/challenges/find-the-running-median/problem
# https://www.youtube.com/watch?v=1CxyVdA_654
# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python/44352853
# https://stackoverflow.com/questions/48255849/how-to-get-the-max-heap-in-python
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
import heapq as hq

arr = [87592
,39913
,29754
,7341
,13823
,11277
,38699
,48439
,97628
,7295
,24386]

# Logn time
def runningMedianHeap(a):

    median_list = []
    min_heap = []
    max_heap = []

    def rebalance():
        # if max heap vs min heap size > 2 -> rebalance (take
        # the root of the other item
        if len(max_heap) - len(min_heap) >= 2:
            hq.heappush(min_heap, -hq.heappop(max_heap))
        if len(min_heap) - len(max_heap) >= 2:
            hq.heappush(max_heap, -hq.heappop(min_heap))

    def add_item(ele):
        # Init
        if len(max_heap) == 0 or len(min_heap) == 0:
            hq.heappush(max_heap, -ele)
        else:
            # if ele smaller than max heap -> insert in max heap
            # if ele larger than min heap -> inser in min heap
            if ele < (-max_heap[0]) or ele <= min_heap[0]:
                hq.heappush(max_heap, -ele)

            if ele > min_heap[0]:
                hq.heappush(min_heap, ele)

    def get_median():
        # if heaps are same size -> take avg
        # if not, take the one with larger size
        if len(min_heap) == len(max_heap):
            avg = (min_heap[0] - max_heap[0]) / 2.0
            median_list.append(avg)

        if len(min_heap) > len(max_heap):
            median_list.append(min_heap[0] / 1.0)

        if len(min_heap) < len(max_heap):
            median_list.append(-max_heap[0] / 1.0)

    # iterate through the array
    for ele in a:

        add_item(ele)
        rebalance()
        get_median()

    return median_list

def runningMedianN2(a):

    median_list = []

    # iterate through the array n^2log(n)
    for i in range(1, len(a) + 1):
        tmpA = a[:i] # n^2

        # sort the array log(n) time
        tmpA = sorted(tmpA)

        isEven = False
        median = 0.0

        # Check length of array if even or odd
        if len(tmpA) % 2 == 0:
            isEven = True

        midPoint = len(tmpA) // 2

        # if odd, takes the middle
        # if even, it's the average
        if isEven:
            median = (tmpA[midPoint] + tmpA[midPoint - 1]) / 2
        else:
            median = tmpA[midPoint]

        median_list.append(median / 1.0)

    return median_list


# print(runningMedian(arr))
# print(runningMedianHeap(arr))

li = [5,1,3,9,5]
# li2 = [5,7,9,1,3]
# li = []
hq.heapify(li) # min heap
print(li)
# print(hq.heappop(li))
# hq.heappush(li, 12)
# hq.heappush(li, -4)
# print(-li[0], -hq.heappop(li))
# print(hq.heappop(li2))
# print(li[0])
# print(li)
# hq.heappushpop(li, 4) # push first
# print(li) # [3, 4, 9, 7, 5]
# print(hq.nlargest(1, li), hq.nsmallest(1, li)) # [9] [3]
# hq.heapreplace(li, 4) # pop first
# print(li) # [3, 4, 9, 7, 5]
# print(hq.nlargest(1, li), hq.nsmallest(1, li)) # [9] [3]
