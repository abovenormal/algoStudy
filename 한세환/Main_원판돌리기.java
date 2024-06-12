import java.io.*;
import java.util.*;

public class Main {
    static int n,m,t;
    static int x,d,k;
    static boolean change;
    static int[][] map;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    static class Node{
        int x,y,v;
        public Node(int x, int y, int v) {
            this.x = x;
            this.y = y;
            this.v = v;
        }

    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        map = new int[n][m];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken()); //x : 몇번째 원판인지
            d = Integer.parseInt(st.nextToken()); //d : (0:시계, 1:반시계)
            k = Integer.parseInt(st.nextToken()); //k : 원판 몇번 회전시킬껀지
            change = false; //true:인접값을 바꾼적있다. false:바꾼적 없다->평균값구하고 +1,-1해줘야함.

            int bea = 1;//배수
            while(true) {
                int xx = (x*bea)-1;//원판=행 -> 인덱스로 취급해야해서 -1해줌.
                if(xx>=n) break;//원판 개수보다 커지면 그만 돌리기.
                rotation(xx);//돌리기
                bea++;
            }

            //원판 요소 하나씩 모두 탐색
            for(int xx=0; xx<n; xx++) {
                for(int yy=0; yy<m; yy++) {
                    BFS(xx,yy,map[xx][yy]);
                }
            }

            //평균값 구해서 +1,-1해줌.
            if(!change) avgMap();
        }


        int sum = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                sum+=map[i][j];
            }
        }
        System.out.println(sum);
    }

    //원판 돌리기 -> 요소값 이동
    public static void rotation(int x) {
        int kk = k;
        if(d==1) kk = m-k;//시계방향으로 바꾸기

        //원판 돌리기 -> x행에 있는 요소값들을 오른쪽으로 kk칸씩 이동.
        while(kk>0) {
            int temp = map[x][m-1];
            for(int i=m-1; i>=1; i--)
                map[x][i] = map[x][i-1];
            map[x][0] = temp;
            kk--;
        }
    }

    //x행y열에 있는 값과 상하좌우에 인접한 값은 모두 0으로 바꾼다.
    public static void BFS(int x, int y, int v) {
        if(v==0) return;//만약 현재 값이 0이면 종료.

        Queue<Node> q = new LinkedList<>();
        boolean[][] check = new boolean[n][m];
        boolean flag = false;//인접값이 하나라도 바뀌면 true로 바뀜.
        check[x][y] = true;
        q.add(new Node(x, y, v));

        while(!q.isEmpty()) {
            Node cur = q.poll();

            for(int i=0; i<4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if(nx<0 || ny<0 || nx>=n || ny>=m) {
                    // ny<0 이다.->현재열이 0열이다.   (x행0열) == (x행m-1열) 이면 인접한거임.
                    if(ny<0 && map[nx][m-1]==cur.v && !check[nx][m-1]) {
                        q.add(new Node(nx, m-1, map[nx][m-1]));
                        map[nx][m-1]=0;
                        check[nx][m-1] = true;
                        flag=true;
                    }
                    //위와 마찬가지 원리
                    else if(ny>=m && map[nx][0]==cur.v && !check[nx][0]) {
                        q.add(new Node(nx, 0, map[nx][0]));
                        map[nx][0]=0;
                        check[nx][m-1] = true;
                        flag=true;
                    }
                    continue;
                }

                //인접값이 같을때
                if(map[nx][ny]==cur.v && !check[nx][ny]) {
                    q.add(new Node(nx,ny,map[nx][ny]));
                    map[nx][ny]=0;
                    check[nx][ny]=true;
                    flag=true;
                }
            }
        }

        if(flag) {//한번이라도 바뀌었으면
            map[x][y]=0;//가장처음에 탐색한값도 0으로 바꿔주기
            change = true;
        }
    }

    //평균값 구해서 +1,1해주기.
    public static void avgMap() {
        double avg=0, cnt=0, sum=0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(map[i][j]==0)continue;
                cnt++;
                sum+=map[i][j];
            }
        }
        avg = sum/cnt;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(map[i][j]==0)continue;
                if(avg<map[i][j]) map[i][j]--;
                else if(avg>map[i][j]) map[i][j]++;
            }
        }
    }
}