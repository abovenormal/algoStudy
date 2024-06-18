import java.io.*;
import java.util.*;

class Main {

    static int K, V, E;
    static BufferedReader br;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] neighbor;
    static String ans;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        K = Integer.parseInt(br.readLine());

        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());

            graph = new ArrayList<ArrayList<Integer>>();

            for (int j = 0; j < V; j++) {
                graph.add(new ArrayList<Integer>());
            }

            ans = "YES";

            for (int j = 0; j < E; j++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken())-1 ;
                int y = Integer.parseInt(st.nextToken())-1;

                graph.get(x).add(y);
                graph.get(y).add(x);
            }

            neighbor = new int[V];

            for (int j = 0; j < V; j++) {
                if (neighbor[j] == 0) {
                    if (!bfs(j)) break;
                }
            }

            System.out.println(ans);
        }
    }

    public static boolean bfs(int n) {

        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);
        neighbor[n] = 1;

        while (!queue.isEmpty()) {
            int node = queue.poll();

            for (Integer i : graph.get(node)) {
                if (neighbor[node] == neighbor[i]) {
                    ans = "NO";
                    return false;
                }
                if(neighbor[i]==0){
                    neighbor[i] = neighbor[node]*(-1);
                    queue.add(i);
                }
            }
        }
        return true;
    }
}