import java.io.*;
import java.util.*;

/* Bot-up 방식
public class Main {
    static int n, k;
    static int[][] items;
    static int[][] dp;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        items = new int[n][2];
        dp = new int[n + 1][k + 1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            items[i][0] = w;
            items[i][1] = v;

        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                if (items[i-1][0] > j) {
                    dp[i][j] = dp[i - 1][j];
                }else{
                   dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1]);
                }
            }
        }
        ans = dp[n][k];
        System.out.println(ans);
    }
}
*/

// Top-down
public class Main {

    static int n, k;
    static int[][] items;
    static Integer[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        items = new int[n][2];
        dp = new Integer[n + 1][k + 1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            items[i][0] = w;
            items[i][1] = v;
        }

        int ans = ks(n - 1, k);
        System.out.println(ans);

    }

    public static int ks(int num, int weight) {
        if (num < 0) {
            return 0;
        }

        int curW = items[num][0];
        int curV = items[num][1];

        if (dp[num][weight] == null) {
            if (curW > weight) {
                dp[num][weight] = ks(num - 1, weight);
            } else {
                dp[num][weight] = Math.max(ks(num- 1, weight), ks(num- 1, weight - curW) + curV);
            }
        }

        return dp[num][weight];

    }

}