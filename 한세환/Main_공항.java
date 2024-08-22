import java.io.*;
import java.util.*;

public class Main {
    static int gates, plane, ans;
    static int[] parent;
    static boolean check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        gates = Integer.parseInt(br.readLine());
        plane = Integer.parseInt(br.readLine());

        parent = new int[gates+1];

        for(int i=0;i<gates+1;i++){
            parent[i] = i;
        }

        for (int i = 0; i < plane; i++) {
            int temp = Integer.parseInt(br.readLine());
            if(find(temp)==0) break;
            ans++;
            union(find(temp),find(temp)-1);
        }

        System.out.println(ans);
    }

    public static void union(int a,int b){
        a = find(a);
        b = find(b);

        parent[a]=b;
    }

    public static int find(int x){
        if(parent[x]==x) return x;
        else return parent[x]=find(parent[x]);
    }

}