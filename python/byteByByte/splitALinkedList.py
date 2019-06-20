# https://www.youtube.com/watch?v=lMxYBLqt1Mg&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=10

# l = 1->2->3->4->5
#        ^r
#      ^n
# one pointer will move twice the other one

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

def splitInHalf(node):
    # check if node is null
    if node == None:
        return None

    # increment runner once then by 2
    # increment list by one
    runner = node.next

    while runner != None:
        runner = runner.next
        if runner == None: break
        runner = runner.next
        node = node.next

    # return second half
    secondPart = node.next
    # cut the first part off
    node.next = None

    return secondPart

def printNode(node):
    print(node.value)
    while node.next:
        node = node.next
        print(node.value)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next = three
three.next = four
four.next = five

splitInHalf(one)

printNode(one)
print("")
printNode(four)
