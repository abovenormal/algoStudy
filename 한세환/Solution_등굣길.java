import java.io.*;
import java.util.*;

class Node {
    int x, y, dist;

    Node(int x, int y, int dist) {
        this.x = x;
        this.y = y;
        this.dist = dist;
    }
}

public class Solution {

    public static int[][] map;
    public static boolean[][] visited;
    public static int[] dx = {1, 0};
    public static int[] dy = {0, 1};
    public static long div = 1000000007;
    public static int cnt;

    public static int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        map = new int[n][m];
        visited = new boolean[n][m];

        bfs(puddles, m, n);

        answer = cnt;

        return answer;
    }

    public static void bfs(int[][] puddles, int m, int n) {
        Queue<Node> queue = new LinkedList<>();
        visited[0][0] = true;
        queue.add(new Node(0, 0, 0));

        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            int curX = curNode.x;
            int curY = curNode.y;
            int curDist = curNode.dist;

            for (int i = 0; i < 2; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];
                int nDist = curDist + 1;
                boolean ifPuddle = true;

                if (nx == n - 1 && ny == m - 1) {
                    int curLastPoint = map[n - 1][m - 1];

                    if (curLastPoint == 0 || curLastPoint == nDist) {
                        map[n - 1][m - 1] = nDist;
                        cnt++;
                    } else if (curLastPoint > curDist) {
                        map[n - 1][m - 1] = nDist;
                        cnt = 1;
                    }
                }


                for (int j = 0; j < puddles.length; j++) {    // 웅덩이 체크

                    if (nx == (puddles[j][0] - 1) && ny == (puddles[j][0] - 1))
                        ifPuddle = false;
                }

                if (!ifPuddle) continue;

                if (nx >= 0 && ny >= 0 && nx < n && ny < m && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    if (map[nx][ny] == 0 || map[nx][ny] <= nDist) {
                        map[nx][ny] = nDist;
                        queue.add(new Node(nx, ny, nDist));
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(solution(4, 3, new int[][]{{2, 2}}));

    }
}