import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {
    private static final char[][] map = new char[5][5];
    private static final boolean[][] visited = new boolean[5][5];
    private static final int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private static int cs = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 5; i++) {
            map[i] = br.readLine().toCharArray();
        }

        dfs(0, 0); //7자리를 선택한다.
        System.out.println(cs);
    }

    private static void dfs(int nowDepth, int start) {
        if (nowDepth == 7) {
            if (checkLinked()) cs++;
        } else {
            for (int i = start; i < 25; i++) {
                visited[i / 5][i % 5] = true;
                dfs(nowDepth + 1, i + 1);
                visited[i / 5][i % 5] = false;
            }
        }
    }

    private static boolean checkLinked() {
        boolean[][] cpyVisited = new boolean[5][5];
        for (int i = 0; i < 5; i++) {
            cpyVisited[i] = visited[i].clone();
        }

        int x = 0, y = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (cpyVisited[i][j]) {
                    x = i;
                    y = j;
                }
            }
        }

        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));

        int cnt = 0;
        int s = 0;
        while (!q.isEmpty()) {
            Point poll = q.poll();

            for (int[] dir : dirs) {
                int mvx = poll.x + dir[0];
                int mvy = poll.y + dir[1];

                if (0 > mvx || 5 <= mvx || 0 > mvy || 5 <= mvy) {
                    continue;
                }

                if (cpyVisited[mvx][mvy]) {
                    if (map[mvx][mvy] == 'S') s++;
                    cnt++;
                    q.add(new Point(mvx, mvy));
                    cpyVisited[mvx][mvy] = false;
                }
            }
        }
        if (cnt == 7 && 4 <= s) {
            return true;
        }
        return false;
    }
}