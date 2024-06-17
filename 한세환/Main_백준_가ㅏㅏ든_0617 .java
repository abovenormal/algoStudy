import java.io.*;
import java.util.*;

class Pos {
    int x;
    int y;
    int time;

    Pos(int x, int y){
        this.x = x;
        this.y = y;
        this.time = 0;
    }
}

class Pair{
    int time;
    int type;
    Pair(){

    }
    Pair(int time, int type){
        this.time = time;
        this.type = type;
    }
}

class Main{
    static int row, col;
    static int green, red;
    static int[][] garden;
    static ArrayList<Pos> possible;
    static boolean[] visited;
    static int[] greens, reds;
    static int max;
    static final int RED = 3;
    static final int GREEN = 4;
    static final int FLOWER = 5;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        st = new StringTokenizer(br.readLine(), " ");

        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());
        green = Integer.parseInt(st.nextToken());
        red = Integer.parseInt(st.nextToken());
        possible = new ArrayList<>();


        garden = new int[row][col];
        for(int i=0; i<row; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<col; j++){
                garden[i][j] = Integer.parseInt(st.nextToken());
                if(garden[i][j] == 2)
                    possible.add(new Pos(i,j));
            }
        }

        greens = new int[green];
        reds = new int[red];
        visited = new boolean[10];
        perm_green(0, 0);
        System.out.println(max);
    }

    private static void perm_green(int start, int r){
        if(r == green){
            perm_red(0, 0);
            return;
        }

        for(int i=start; i<possible.size(); i++){
            if(!visited[i]){
                visited[i] = true;
                greens[r] = i;
                perm_green(i+1, r+1);
                visited[i] = false;
            }
        }
    }

    private static void perm_red(int start, int r){
        if(r == red){
            // 배양액 퍼트리기
            bfs();
            return;
        }

        for(int i=start; i<possible.size(); i++){
            if(!visited[i]){
                visited[i] = true;
                reds[r] = i;
                perm_red(i+1, r+1);
                visited[i] = false;
            }
        }
    }

    private static void bfs(){
        Queue<Pos> q = new LinkedList<>();
        Pair[][] state = new Pair[row][col];

        // state 초기화
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
                state[i][j] = new Pair();

        // 배양지로 선택한 곳에 배양액 놓기
        for(int i=0; i<red; i++){
            Pos p = possible.get(reds[i]);
            state[p.x][p.y] = new Pair(0, RED);
            q.offer(new Pos(p.x, p.y));
        }
        for(int i=0; i<green; i++){
            Pos p = possible.get(greens[i]);
            state[p.x][p.y] = new Pair(0, GREEN);
            q.offer(new Pos(p.x, p.y));
        }

        int sum = 0;
        // 위, 아래, 왼쪽, 오른쪽
        int[] xdir = {-1,1,0,0};
        int[] ydir = {0,0,-1,1};

        while(!q.isEmpty()){
            Pos p =q.poll();
            int x = p.x;
            int y = p.y;
            int curtime = state[x][y].time;
            int curtype = state[x][y].type;
            // 꽃이 핀 자리라면 퍼지지 않음
            if(state[x][y].type == FLOWER) continue;
            // 4 방향으로 퍼트리기
            for(int i=0; i<4; i++){
                int dx = x + xdir[i];
                int dy = y + ydir[i];
                // 유효한 위치이고 호수가 아닌 경우
                if(isValidPosition(dx, dy) && garden[dx][dy] != 0){
                    // 아직 배양액이 퍼지지 않았다면 퍼트림
                    if(state[dx][dy].type == 0){
                        state[dx][dy] = new Pair(curtime+1, curtype);
                        q.offer(new Pos(dx, dy));
                    }
                    // 빨간색이 있을때 초록색이 퍼지는 거라면 꽃을 피우고 count
                    else if(state[dx][dy].type == RED){
                        if(curtype == GREEN && state[dx][dy].time == curtime + 1){
                            sum++;
                            state[dx][dy].type = FLOWER;
                        }
                    }
                    // 초록색이 있을때 빨간색이 퍼지는 거라면 꽃을 피우고 count
                    else if(state[dx][dy].type == GREEN){
                        if(curtype == RED && state[dx][dy].time == curtime + 1){
                            sum++;
                            state[dx][dy].type = FLOWER;
                        }
                    }
                }
            }
        }
        // max 값 update
        max = max < sum ? sum : max;
    }

    private static boolean isValidPosition(int x, int y){
        if(x < 0 || y < 0 || x >= row || y >= col) return false;
        return true;
    }
}