import java.io.*;
import java.util.*;

public class Main3{

    static int[] arr;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        arr = new int[n];
        dp = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i =0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i =0;i<n;i++){
            dp[i] =1 ;

            for(int j=0;j<i;j++){
                if(arr[j]<arr[i] && dp[i]<dp[j]+1){
                    dp[i] = dp[j]+1;
                }
            }
        }

        int max =Integer.MIN_VALUE;

        for(int i=0;i<n;i++){
            max = Math.max(max,dp[i]);
        }
        System.out.println(max);
    }
}