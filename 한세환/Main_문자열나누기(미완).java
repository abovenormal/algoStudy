import java.io.*;
import java.util.*;

public class Main {

    static int[][][] dp = new int[2501][2501][2];
    static char[] str = new char[2501];
    static final int MOD = 1000000007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        String input = br.readLine();

        str = input.toCharArray();

        if (str[1] == '0') {
            dp[1][1][1] = 1;
        }
        else if (str[1] != '0') {
            dp[1][1][0] = 1;
        }

        for(int i = 2; i <N;i++){
            for(int j =1;j<i;i++){
                if (str[i] == '0') {
                    dp[i][j][0] = dp[i - 1][j][0];
                    dp[i][j][1] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]) % MOD;
                }
                else if (str[i] != '0') {
                    dp[i][j][0] = ((dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]) % MOD + dp[i - 1][j][0]) % MOD;
                }
            }
        }

        System.out.println((dp[N][K][0] + dp[N][K][1]) % MOD);

    }


}