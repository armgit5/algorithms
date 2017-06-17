Nodes = 0
Edges = 0

with open('even_tree.txt') as f:
    Nodes, Edges = map(int, next(f).split())

    class Graph:

        def __init__(self):
            self.size = 1
            self.parent = None

        def add_parent(self, parent):
            self.parent = parent
            while parent != None:
                parent.size += 1
                parent = parent.parent


    if __name__ == "__main__":
        nodes_list = [Graph() for _ in xrange(Nodes)]
        even_tree_count = 0
        for _ in xrange(Edges):
            child, parent = map(int, next(f).split())
            # print child, parent
            nodes_list[child - 1].add_parent(nodes_list[parent - 1])

        for node in nodes_list:
            print  node.size
            if node.size % 2 == 0 and node.parent != None:
                even_tree_count += 1

        print even_tree_count