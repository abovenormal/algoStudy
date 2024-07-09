import java.io.*;
import java.util.*;


public class Main {

    static int n;
    static int[] arr = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    static List<Long> list = new ArrayList<>();

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        dfs(0,0) ;
        Collections.sort(list);

        try{
            System.out.println(list.get(n-1));
        }catch(Exception e){
            System.out.println(-1);
        }


    }

    public static void dfs(long num, int idx) {
        if(!list.contains(num)){
            list.add(num);
        }

        if(idx>=10){
            return;
        }

        dfs((num*10)+arr[idx],idx+1);
        dfs(num,idx+1);
    }

}