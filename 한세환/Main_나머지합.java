import java.io.*;
import java.util.*;


public class Main {

    static int n, m;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());

        int amt = 0;
        for (int i = 0; i < n; i++) {
            amt += Integer.parseInt(st.nextToken());
            arr[i] = amt;
        }

        for (int i = 0; i < n; i++) {
            if (arr[i] % 3 == 0) {
                answer++;
                //System.out.println(arr[i]);
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = arr[j] - arr[i-1];
                if (temp % 3 == 0 && temp != 0) {
                    answer++;
                    //System.out.println(i+ " " + j +" " + temp);
                }
            }
        }

        System.out.println(answer);

    }
}