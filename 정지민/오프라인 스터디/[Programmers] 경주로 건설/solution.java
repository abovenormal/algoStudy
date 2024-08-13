import java.util.*;

class Node {
    int x;
    int y;
    int direct;

    Node(int x, int y, int direct) {
        this.x = x;
        this.y = y;
        this.direct = direct;
    }
}

class Solution {

    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,-1,0,1};
    static int INF = (int) Math.pow(10, 9);

    public int get_direct(int cx, int cy, int nx, int ny) {
        // 동
        if (cx == nx && cy < ny)
            return 0;
        // 서
        else if (cx == nx && cy > ny)
            return 1;
        // 남
        else if (cx < nx && cy == ny)
            return 2;
        // 북
        else
            return 3;
    }

    public int bfs(int[][] board, int start_x, int start_y, int n) {
        Queue<Node> q = new LinkedList<>();
        int[][][] visited = new int[n][n][4];
        for (int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                for(int k=0; k<4; k++)
                    visited[i][j][k] = INF;

        q.add(new Node(start_x, start_y, 0));
        q.add(new Node(start_x, start_y, 2));
        visited[start_x][start_y][0] = 0;
        visited[start_x][start_y][2] = 0;

        while (!q.isEmpty()) {
            Node cur = q.poll();

            for(int i=0; i<4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx<0 || nx>=n || ny<0 || ny>=n) continue;
                if (board[nx][ny] == 1) continue;

                int ndirect = get_direct(cur.x, cur.y, nx, ny);

                int cur_cost = visited[cur.x][cur.y][cur.direct];
                int add_cost = 0;
                if (cur.direct == ndirect)      // 직선
                    add_cost = 100;
                else                            // 커브
                    add_cost = 600;

                if (visited[nx][ny][ndirect] < cur_cost + add_cost) continue;

                visited[nx][ny][ndirect] = cur_cost + add_cost;
                q.add(new Node(nx, ny, ndirect));
            }
        }

        int res = INF;
        for(int i=0; i<4; i++)
            res = Math.min(res, visited[n-1][n-1][i]);
        return res;
    }

    public int solution(int[][] board) {
        int answer = bfs(board, 0, 0, board.length);
        return answer;
    }
}