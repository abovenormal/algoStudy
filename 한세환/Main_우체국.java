import java.io.*;
import java.util.*;

public class Main {
    static int N, res;
    static int[][] arr;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        arr = new int[N][2];
        long sum = 0;
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());   //위치
            int a = Integer.parseInt(st.nextToken());   //인구수
            arr[i][0] = x;
            arr[i][1] = a;
            sum += a;
        }

        long middle = (sum+1)/2;

        Arrays.sort(arr, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        long idx = 0;
        for(int i=0; i<N; i++) {
            idx += arr[i][1];
            if(idx >= middle) {
                res = arr[i][0];
                break;
            }
        }

        System.out.println(res);
    }
}