package Graph;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Graph<T>{

    private List<Edge<T>> allEdges;
    private Map<T, Node<T>> allNodes;
    private boolean isDirected = false;

    public Graph(boolean isDirected) {
        allEdges = new ArrayList<Edge<T>>();
        allNodes = new HashMap<T, Node<T>>();
        this.isDirected = isDirected;
    }

    public void addEdge(T id1, T id2, Integer weight) {
        Node<T> node1, node2 = null;

        if (allNodes.containsKey(id1)) {
            node1 = allNodes.get(id1);
        } else {
            node1 = new Node<T>(id1);
            allNodes.put(id1, node1);
        }

        if (allNodes.containsKey(id2)) {
            node2 = allNodes.get(id2);
        } else {
            node2 = new Node<T>(id2);
            allNodes.put(id2, node2);
        }

        Edge<T> edge = new Edge<T>(node1, node2, weight, isDirected);
        allEdges.add(edge);
        node1.addAdjacentNode(edge, node2);

        if (isDirected == false) {
            node2.addAdjacentNode(edge, node1);
        }
    }

    public List<Edge<T>> getAllEdges() {
        return allEdges;
    }

    public Map<T, Node<T>> getAllNodes() {
        return allNodes;
    }

    public void setDataForNode(T id, T data) {
        if (allNodes.containsKey(id)) {
            Node<T> node = allNodes.get(id);
            node.setData(data);
        }
    }

    public Node<T> getNode(T id) {
        return  getAllNodes().get(id);
    }

    public void printString() {
        for (Edge<T> edge:
             allEdges) {
            System.out.print(edge.getNode1());
            System.out.print(edge.getNode2());
            System.out.println(edge.getWeight());
        }
    }
}

class Edge<T> {

    private boolean isDirected = false;
    private Node<T> node1;
    private Node<T> node2;
    private int weight;

    public Edge(Node<T> node1, Node<T> node2, Integer weight, boolean isDirected) {
        this.isDirected = isDirected;
        this.node1 = node1;
        this.node2 = node2;
        this.weight = weight;
    }

    public Node<T> getNode1() {
        return node1;
    }

    public Node<T> getNode2() {
        return node2;
    }

    public int getWeight() {
        return weight;
    }
}

class Node<T> {
    T id;
    int parentDist = 0;
    private T data;
    private List<Edge<T>> edges = new ArrayList<>();
    private List<Node<T>> adjacentNodes = new ArrayList<>();

    public Node(T id) {
        this.id = id;
    }

    public void addAdjacentNode(Edge<T> edge, Node<T> node) {
        edges.add(edge);
        adjacentNodes.add(node);
    }

    public List<Node<T>> getAdjacentNodes() {
         return adjacentNodes;
    }

    public List<Edge<T>> getEdges() {
        return edges;
    }

    public void setData(T data) {
        this.data = data;
    }
}