import java.util.*;
import java.io.*;

class Main {

    static int n,m,d;
    static int[][] _map;
    static List<ArrayList<Integer>> player_pos = new ArrayList<ArrayList<Integer>>();
    static int[] dx = {0,-1,0};
    static int[] dy = {-1,0,1};

    static class Node {
        int x;
        int y;
        int cnt;

        Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    static class NodeComparator implements Comparator<Node> {
        @Override
        public int compare(Node o1, Node o2) {
            if (o1.cnt == o2.cnt) {
                return o1.y - o2.y;
            }
            return o1.cnt - o2.cnt;
        }
    }

    static void combinations(int[] arr, int[] out, int startIdx, int depth, int r) {
        if (depth == r) {
            ArrayList<Integer> combi = new ArrayList<>();
            for(int num : out) {
                combi.add(num);
            }
            player_pos.add(combi);
            return;
        }

        for(int i=startIdx; i<arr.length; i++) {
            out[depth] = arr[i];
            combinations(arr, out, i+1, depth+1, r);
        } 
    }

    static boolean check_end(int[][] _map) {
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if (_map[i][j] == 1)
                    return false;
            }
        }
        return true;
    }

    // start 에서 출발해 거리 D 이하인 적들 중 가장 가까운 거리의 적 찾기
    static Node bfs(Node start, int[][] _map) {
        PriorityQueue<Node> pq = new PriorityQueue<>(1, new NodeComparator());
        boolean[][] visited = new boolean[n][m];
        visited[start.x][start.y] = true;
        pq.offer(start);

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (_map[cur.x][cur.y] == 1) {
                return cur;
            }

            for(int i=0; i<3; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx<0 || nx>=n || ny<0 || ny>=m) continue;

                if (!visited[nx][ny] && cur.cnt + 1 < d) {
                    pq.add(new Node(nx, ny, cur.cnt+1));
                    visited[nx][ny] = true;
                }
            }
        }

        // 공격할 적 못찾으면, (-1, -1) 리턴
        return new Node(-1,-1,-1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        _map = new int[n][m];
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<m; j++) {
                _map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] arr = new int[m];
        for(int i=0; i<m; i++)
            arr[i] = i;
        combinations(arr, new int[3], 0, 0, 3);

        int answer = 0;
        for(ArrayList<Integer> player : player_pos) {
            int[][] temp_map = new int[n][m];
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {
                    temp_map[i][j] = _map[i][j];
                }
            }

            int destroyed_cnt = 0;
            
            // 모든 적이 격자판에서 제외될때까지 공격
            while (check_end(temp_map) == false) {
                // 모든 궁수 동시 공격
                // 각각의 궁수 위치에서 bfs -> 거리 D 이하인 적들 중 가장 가까운 거리의 적 찾기 -> 왼쪽에 있는 적부터 공격
                List<Node> destroyed = new ArrayList<Node>();
                for (int py : player) {
                    Node _destroyed = bfs(new Node(n-1, py, 0), temp_map);
                    if (_destroyed.x != -1) {
                        destroyed.add(_destroyed);
                    }
                }

                for (Node _destroyed : destroyed) {
                    if (temp_map[_destroyed.x][_destroyed.y] != 0) {
                        temp_map[_destroyed.x][_destroyed.y] = 0;
                        destroyed_cnt += 1;
                    }
                }

                // 적 이동
                for(int i=n-1; i>0; i--) {
                    for(int j=0; j<m; j++) {
                        temp_map[i][j] = temp_map[i-1][j];
                    }
                }
                for(int j=0; j<m; j++) {
                    temp_map[0][j] = 0;
                }
            }

            answer = Math.max(answer, destroyed_cnt);
        }

        System.out.println(answer);
    }
}
