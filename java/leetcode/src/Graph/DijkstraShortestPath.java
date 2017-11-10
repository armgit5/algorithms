package Graph;

import java.util.*;

public class DijkstraShortestPath {

//    public Node<Integer> neighborNode(Node<Integer> currNode, Node<Integer> node1, Node<Integer> node2) {
//        if (currNode != node1) {
//            return node1;
//        } else {
//            return node2;
//        }
//    }

    public int[] findShortest(Graph<Integer> graph) {

        int nodeLenth = graph.getAllNodes().size();
        int[] prev = new int[nodeLenth];
        int[] dist = new int[nodeLenth];
        boolean[] visited = new boolean[nodeLenth];
        for (int i = 0; i < nodeLenth; i++) {
            dist[i] = Integer.MAX_VALUE;
            prev[i] = -1;
            visited[i] = false;
        }

        dist[0] = 0;
        PriorityQueue<Integer> Q = new PriorityQueue<Integer>();
        int firstNodeId = graph.getAllNodes().get(0).id;
        Q.add(firstNodeId);

        while (!Q.isEmpty()) {
            int currNodeId = Q.poll();
            visited[currNodeId] = true;
            List<Edge<Integer>> neighborEdges = graph.getAllNodes().get(currNodeId).getEdges();

            for (Edge<Integer> edge:
                 neighborEdges) {
                Node<Integer> node2 = edge.getNode2();
                Node<Integer> neighborNode = node2;
                int weight = edge.getWeight();

                if (!visited[neighborNode.id]) {
                    int alt = dist[currNodeId] + weight;
                    if (alt < dist[neighborNode.id]) {
                        dist[neighborNode.id] = alt;
                        prev[neighborNode.id] = currNodeId;
                        dist[neighborNode.id] = alt;
                        Q.add(neighborNode.id);
                    }
                }
            }
        }

        return dist;
    }

    public static void main(String args[]) {
        Graph<Integer> graph = new Graph<Integer>(false);
        graph.addEdge(0,1,3);
        graph.addEdge(0,2,4);
        graph.addEdge(1,3,4);
        graph.addEdge(1,4,6);
        graph.addEdge(2,4,6);
        graph.addEdge(3,5,5);
        graph.addEdge(4,5,7);
        graph.addEdge(4,6,5);

        DijkstraShortestPath d = new DijkstraShortestPath();
        int[] list = d.findShortest(graph);
        for (int i:
             list) {
            System.out.println(i);
        }
    }
}
