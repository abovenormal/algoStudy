import java.io.*;
import java.util.*;

class Node {
    int x,y;

    Node(int x , int y){
        this.x = x;
        this.y = y;
    }
}
public class Main {

    static int N, M;
    static int[][] map;
    static boolean[] visited;
    static ArrayList<Node> houses = new ArrayList<>();
    static ArrayList<Node> chicken = new ArrayList<>();
    static ArrayList<Node> choice = new ArrayList<>();
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];

        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                int temp = Integer.parseInt(st.nextToken());
                map[i][j] = temp;

                if(temp==1) houses.add(new Node(i,j));
                else if (temp==2) {
                    chicken.add(new Node(i,j));
                }
            }
        }

        visited = new boolean[chicken.size()];
        back(0,0);
        System.out.println(res);

    }

    public static void back(int depth , int start){
        if(depth == M){
            int sum = 0 ;
            for(Node curN : houses){
                int min = Integer.MAX_VALUE;

                for(Node curChicken : choice){
                    int temp = Math.abs(curChicken.x - curN.x) + Math.abs(curChicken.y - curN.y);
                    min = Math.min(min,temp);
                }
                sum += min;
            }
            res = Math.min(res,sum);
            return;
        }

        for(int i =start ;i<chicken.size();i++){
            if(!visited[i]){
                choice.add(chicken.get(i));
                back(depth+1, i+1);
                choice.remove(choice.size()-1);
                visited[i]= false;
            }
        }
    }
}