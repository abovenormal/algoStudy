import java.util.*;

class Node {
    int node;
    int dist;
    
    Node(int node, int dist) {
        this.node = node;
        this.dist = dist;
    }
}

class NodeComparator implements Comparator<Node> {
    @Override
    public int compare(Node o1, Node o2) {
        if (o1.dist == o2.dist) {
            return o1.node - o2.node;
        }
        return o1.dist - o2.dist;
    }
}

class Solution {
    
    static int INF = Integer.MAX_VALUE;
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        List<ArrayList<Node>> graph = new ArrayList<>();
        for(int i=0; i<edge.length; i++) {
            graph.add(new ArrayList<>());
        }
        for(int i=0; i<edge.length; i++) {
            int v1 = edge[i][0];
            int v2 = edge[i][1];
            graph.get(v1).add(new Node(v2, 1));
            graph.get(v2).add(new Node(v1, 1));
        }
        
        int[] distance = new int[n+1];
        Arrays.fill(distance, INF);
        distance[1] = 0;
        
        PriorityQueue<Node> q = new PriorityQueue<>(new NodeComparator());
        q.offer(new Node(1, 0));
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            
            if (distance[cur.node] < cur.dist) continue;
            
            for (Node next : graph.get(cur.node)) {
                if (cur.dist + next.dist < distance[next.node]) {
                    distance[next.node] = cur.dist + next.dist;
                    q.offer(new Node(next.node, cur.dist + next.dist));
                }
            }
        }
        
        int max_dist = 0;
        for(int i=1; i<n+1; i++) {
            max_dist = Math.max(max_dist, distance[i]);
        }
        for(int i=1; i<n+1; i++) {
            if (distance[i] == max_dist) answer++;
        }
        return answer;
    }
}