
class Node():
    def __init__(self, weight=0, key=None):
        self.weight = weight
        self.key = key


class BinaryMinHeap():

    def __init__(self):
        self.allNodes = []
        self.nodePosition = {}

    def swap(self, node1, node2):
        key = node1.key
        weight = node1.weight

        node1.key = node2.key
        node1.weight = node2.weight

        node2.key = key
        node2.weight = weight

    def updatePositionMap(self, key1, key2, pos1, pos2):

        self.nodePosition[key1] = pos1
        self.nodePosition[key2] = pos2

    def add(self, weight, key):
        node = Node(weight, key)
        self.allNodes.append(node)
        currentIndex = len(self.allNodes) - 1
        parentIndex = (currentIndex - 1) / 2

        self.nodePosition[node.key] = currentIndex

        while parentIndex >= 0:
            parentNode = self.allNodes[parentIndex]
            currentNode = self.allNodes[currentIndex]

            if parentNode.weight > currentNode.weight:
                self.swap(parentNode, currentNode)
                self.updatePositionMap(parentNode.key, currentNode.key, parentIndex, currentIndex)
                currentIndex = parentIndex
                parentIndex = (parentIndex - 1) / 2
            else:
                break

    def decrease(self, weight, key):
        currentIndex = self.nodePosition[key]
        self.allNodes[currentIndex].weight = weight
        parentIndex = (currentIndex - 1) / 2

        while parentIndex >= 0:

            parentNode = self.allNodes[parentIndex]
            currentNode = self.allNodes[currentIndex]

            a = parentNode.weight
            b = currentNode.weight

            if parentNode.weight > currentNode.weight:
                self.swap(parentNode, currentNode)
                self.updatePositionMap(parentNode.key, currentNode.key, parentIndex, currentIndex)
                currentIndex = parentIndex
                parentIndex = (parentIndex - 1) / 2
            else:
                break

    def extractMinNode(self):
        if len(self.allNodes) == 1:
            pos = self.allNodes.pop().key
            self.nodePosition.pop(pos)
            return pos
        node = self.extractMinNodeHelper()
        return node.key

    def extractMinNodeHelper(self):
        minNode = Node(self.allNodes[0].weight, self.allNodes[0].key)
        self.nodePosition.pop(minNode.key)

        # replace root with last element
        self.allNodes[0].weight = self.allNodes[-1].weight
        self.allNodes[0].key = self.allNodes[-1].key
        self.allNodes.pop()
        self.nodePosition[self.allNodes[0].key] = 0

        currentIndex = 0
        size = len(self.allNodes)-1

        while True:
            leftIndex = 2 * currentIndex + 1
            rightIndex = 2 * currentIndex + 2

            if leftIndex > size:
                break

            if rightIndex > size:
                rightIndex = leftIndex

            smallerIndex = leftIndex if self.allNodes[leftIndex].weight <=  \
                           self.allNodes[rightIndex].weight else rightIndex
            if self.allNodes[currentIndex].weight > self.allNodes[smallerIndex].weight:
                parentNode = self.allNodes[currentIndex]
                currentNode = self.allNodes[smallerIndex]
                self.swap(parentNode, currentNode)
                self.updatePositionMap(parentNode.key, currentNode.key, currentIndex, smallerIndex)
                currentIndex = smallerIndex
            else:
                break
        return minNode

    def contain(self, key):
        return key in self.nodePosition

    def printHeap(self):
        for n in self.allNodes:
            print(n.key, n.weight)

    def printPositionMap(self):
        print(self.nodePosition)

    def empty(self):
        return len(self.allNodes) == 0

    def getWeight(self, key):
        if key in self.nodePosition:
            position = self.nodePosition[key]
            return self.allNodes[position].weight
        else:
            return None



# heap = BinaryMinHeap()
# heap.add(-1, "A")
# heap.add(2, "B")
# heap.add(6, "C")
# heap.add(4, "D")
# heap.add(5, "E")
# heap.add(7, "F")
# heap.add(8, "G")

# heap.printHeap()
# heap.printPositionMap()

# heap.decrease(-2, "F")
# heap.printHeap()
# heap.printPositionMap()
# print heap.contain("A")
# print heap.extractMinNode()
# heap.printHeap()
# heap.printPositionMap()