import java.util.*;

class Solution {
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    public int solution(int n, int[][] edge) {
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int[] x : edge) {
            graph.get(x[0]).add(x[1]);
            graph.get(x[1]).add(x[0]);
        }
        boolean[] visited = new boolean[n + 1];
        int answer = bfs(graph, visited, n);
        return answer;
    }

    public int bfs(ArrayList<ArrayList<Integer>> graph,
                   boolean[] visited, int n) {
        Queue<Integer> queue = new LinkedList<>();
        int[] depth = new int[n + 1];
        queue.add(1);
        visited[1] = true;
        depth[1] = 1;
        while (!queue.isEmpty()) {
            int x = queue.poll();
            for (int i = 0; i < graph.get(x).size(); i++) {
                int next = graph.get(x).get(i);
                if (!visited[next]) {
                    visited[next] = true;
                    depth[next] += depth[x] + 1;
                    queue.add(next);
                }
            }
        }
        int m = Arrays.stream(depth).max().getAsInt();
        int answer = 0;
        for (int x : depth) {
            if (x == m) {
                answer++;
            }
        }
        return answer;
    }
}