import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new int[m];

        bt(0, 1, m);
    }

    public static void bt(int depth, int start, int limit) {
        if (depth == limit) {
            for (int i = 0; i < m; i++) {
                System.out.print((visited[i]) + " ");
            }
            System.out.println();

            return;
        }

        for (int i = start; i <= n; i++) {
            visited[depth] = i;
            bt(depth + 1, i, limit);

        }
    }
}