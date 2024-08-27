import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited,done;
    static int[] arr;
    static int res;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            int len = Integer.parseInt(br.readLine());
            res = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());

            arr = new int[len + 1];
            visited = new boolean[len + 1];
            done = new boolean[len + 1];

            for (int j = 1; j <= len; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 1; j <= len; j++) {
                dfs(j);
            }
            System.out.println(len - res);

        }
    }

    public static void dfs(int x) {
        if(done[x]) return;
        if(visited[x]){
            done[x] = true;
            res++;
            //System.out.println(x + " "+ res);
        }

        visited[x] = true;
        dfs(arr[x]);
        done[x] = true;
        visited[x] = false;
    }
}