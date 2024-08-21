import java.io.*;
import java.util.*;

public class Main22 {
    static int gates, plane, ans;
    static boolean[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        gates = Integer.parseInt(br.readLine());
        plane = Integer.parseInt(br.readLine());

        int smallestNo = 1;
        arr = new boolean[gates];

        for (int i = 0; i < plane; i++) {
            int temp = Integer.parseInt(br.readLine());

            if(!arr[temp-1]){
                arr[temp-1] = true;
                ans++;
            }else if (!arr[smallestNo-1]){
                if(smallestNo<temp){
                    arr[smallestNo-1] = true;
                    smallestNo++;
                    ans++;
                }
            }else{
                break;
            }
        }

        System.out.println(ans);
    }
}