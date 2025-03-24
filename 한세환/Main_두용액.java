import java.io.*;
import java.util.*;

// Bj 2470 두 용액

public class Main{
    static int n;
    static List<Integer> list = new ArrayList<>();
    static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n  = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for(int i=0;i<n;i++){
            list.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(list);

        arr = list.stream().mapToInt(Integer::intValue).toArray();

        int s = 0;
        int e = n-1;
        int min = Integer.MAX_VALUE;
        int alka=0;
        int acid=0;

        while(s<e){
            int cur = arr[s]+arr[e];

            if(min >Math.abs(cur)){
                min = Math.abs(cur);
                alka = arr[s];
                acid = arr[e];
                if(min==0) break;
            }
            if(cur>0) e--;
            else s++;
        }

        System.out.println(alka+" "+acid);



    }
}