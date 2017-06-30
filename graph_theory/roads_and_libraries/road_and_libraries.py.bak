def raw_input():
    return next(f)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, node_from, node_to):
        self.node_from = node_from
        self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.count = 1

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)



    def dfs_helper(self, start_node):
        """TODO: Write the helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """

        # Your code here
        start_node.visited = True


        out_edges = [edge for edge in start_node.edges
                     if edge.node_to.value != start_node.value]
        for edge in out_edges:
            if edge.node_to.visited == False:
                self.count += 1
                self.dfs_helper(edge.node_to)



    def dfs(self, start_node):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        return self.dfs_helper(start_node)



with open('road_and_libraries3.txt') as f:

    q = int(raw_input().strip())

    for a0 in xrange(q):

        graph = Graph()
        graph._clear_visited()

        n, m, x, y = raw_input().strip().split(' ')
        n, m, x, y = [int(n), int(m), int(x), int(y)]
        for a1 in xrange(m):
            city_1, city_2 = raw_input().strip().split(' ')
            city_1, city_2 = [int(city_1), int(city_2)]

            graph.insert_edge(city_1, city_2)
            graph.insert_edge(city_2, city_1)


        total_cost = 0

        for i in range(n):
            if graph.nodes[i].visited == False:

                graph.count = 1
                graph.dfs(graph.nodes[i])

                total_cost += x

                if x > y:
                    total_cost += (graph.count - 1) * y
                else:
                    total_cost += (graph.count - 1) * x

        print total_cost


