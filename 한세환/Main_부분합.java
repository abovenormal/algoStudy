import java.io.*;
import java.util.*;

public class Main {
    static int n, s;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        arr = new int[n+1];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int min = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;
        int tot = 0;
        while(start<=n && end<=n){
            if(tot>=s && min>end-start){
                min = end-start;
            }
            if(tot<s)
                tot += arr[end++];
            else
                tot -= arr[start++];
        }

        if(min==Integer.MAX_VALUE)
            System.out.println("0");
        else
            System.out.println(min);


    }
}