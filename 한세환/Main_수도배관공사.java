import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n, m;

        String[] s = br.readLine().split(" ");

        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);

        int[][]arr =new int [m][2];

        for(int i=0; i<m; i++){
            String[] s1 = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(s1[0]);
            arr[i][1] = Integer.parseInt(s1[1]);
        }

        int [] dp = new int[n+1];

        dp[0] = Integer.MAX_VALUE;
        for(int i=0; i<m; i++){
            for(int j=n; j>=arr[i][0]; j--){
                dp[j] = Math.max(dp[j],Math.min(dp[j-arr[i][0]],arr[i][1]));
            }
        }
        System.out.println(dp[n]);
    }
}