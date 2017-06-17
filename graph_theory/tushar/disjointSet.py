
class Node():
    def __init__(self, data=None, rank=0):
        self.rank = rank
        self.parent = None
        self.data = data


class DisjointSet():

    def __init__(self):
        self.hashMap = {}

    def makeSet(self, data):
        node = Node(data)
        node.parent = node
        self.hashMap[data] = node

    def union(self, data1, data2):
        node1 = self.hashMap[data1]
        node2 = self.hashMap[data2]

        parent1 = self.findSetHelper(node1)
        parent2 = self.findSetHelper(node2)

        if parent1 == parent2:
            return
        if parent1.rank >= parent2.rank:
            parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
            parent2.parent = parent1
        else:
            parent1.parent = parent2

        return True

    def findSet(self, data):
        return self.findSetHelper(self.hashMap[data]).data

    def findSetHelper(self, node):
        if node == node.parent:
            return node

        node.parent = self.findSetHelper(node.parent)
        return node.parent







