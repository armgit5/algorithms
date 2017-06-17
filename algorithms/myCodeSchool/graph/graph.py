class Node():

    def __init__(self, id=None):
        self.id = id
        self.next = None

class Graph():

    def __init__(self):
        self.nodeList = []

    def addNode(self, id):
        node = Node(id)
        self.nodeList.append(node)
        return node

    def addEdge(self, id1, id2):

        node1Found, node2Found = False, False
        node1, node2 = None, None

        for i in xrange(len(self.nodeList)):
            if self.nodeList[i].id == id1:
                node1Found = True
                node1 = self.nodeList[i]
            if self.nodeList[i].id == id2:
                node2Found = True
                node2 = self.nodeList[i]
            if node1Found and node2Found:
                break

        if node1Found == False:
            node1 = self.addNode(id1)

        if node2Found == False:
            node2 = self.addNode(id2)



        temp = Node(id2)
        temp.next = node1.next
        node1.next = temp

    def getNode(self, id):
        for i in range(len(self.nodeList)):
            if id == self.nodeList[i].id:
                return self.nodeList[i]

    def printGraph(self):
        for i in xrange(len(self.nodeList)):
            curr = self.nodeList[i]
            while curr != None:
                print curr.id
                curr = curr.next

            print ""