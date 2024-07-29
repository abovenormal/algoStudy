import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static class Edge implements Comparable<Edge> {
        int to;
        long cost;

        public Edge(int to, long cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return Long.compare(cost, o.cost);
        }
    }

    static List<Edge>[] graph;
    static long[] distA, distB;
    static int N, M, A, B;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
//        System.setIn(Files.newInputStream(Paths.get("src/input.txt")));
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        graph = new List[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()),
                    c = Integer.parseInt(st.nextToken());
            // 양방향 도로 이므로 a에서 b로 가는 간선과 b에서 a로 가는 간선 추가
            graph[a].add(new Edge(b, c));
            graph[b].add(new Edge(a, c));

        }
        // A에서 출발하는 거리를 기록하는 배열 Long.MAX_VALUE로 초기화
        distA = new long[N + 1];
        distB = new long[N + 1];
        // B에서 출발하는 거리를 기록하는 배열 Long.MAX_VALUE로 초기화
        Arrays.fill(distA, Long.MAX_VALUE);
        Arrays.fill(distB, Long.MAX_VALUE);
        dijkstra(A, B, distA);
        dijkstra(B, A, distB);
        StringBuilder sb = new StringBuilder();
        int size = 0;
        for (int i = 1; i < N + 1; i++) {
            if (distA[i] + distB[i] == distA[B]) {
                size++;
                sb.append(i).append(" ");
            }
        }
        bw.write(size + "\n");
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    static void dijkstra(int from, int to, long[] dist) {
        pq.add(new Edge(from, 0));
        dist[from] = 0;
        while (!pq.isEmpty()) {
            Edge current = pq.poll();
            if (current.cost > dist[current.to]) {
                continue;
            }
            if (current.to == to) {
                pq.clear();
                break;
            }
            for (Edge next : graph[current.to]) {
                long nextCost = dist[current.to] + next.cost;
                if (nextCost > dist[next.to]) {
                    continue;
                }
                dist[next.to] = nextCost;
                pq.add(new Edge(next.to, nextCost));
            }
        }
    }
}