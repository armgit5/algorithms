arr =  [25,16,24,5,11,19,1,2,3,5]

class MaxHeap:
    def __init__(self, items=[]):
        self.heap = []
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(0, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(0)
        elif len(self.heap) == 2:
            max = self.heap.pop(0)
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index < 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

m = MaxHeap([95,3])
# m.push(10)
print(str(m.heap[0:len(m.heap)]))
m.pop()
print(str(m.heap[0:len(m.heap)]))

print("")
m = MaxHeap(arr)
print(str(m.heap[0:len(m.heap)]))