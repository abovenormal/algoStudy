import java.util.*;

class Solution {
    
    static class Node {
        int x;
        int y;
        
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    static int n;
    static int m;
    
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,-1,0,1};
    
    static List<Integer> group_amount = new ArrayList<>();
    static Map<Integer, Set<Integer>> col_groups = new HashMap<Integer, Set<Integer>>();
        
    public void bfs(int start_x, int start_y, int[][] land, int[][] visited, int group_num) {
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(start_x, start_y));
        visited[start_x][start_y] = group_num;
        
        int group_cnt = 0;
        while (!q.isEmpty()) {
            Node cur = q.poll();
            group_cnt += 1;
            
            for(int i=0; i<4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if (nx<0 || nx>=n || ny<0 || ny>=m) continue;
                
                if(land[nx][ny] == 1 && visited[nx][ny] == -1) {
                    q.add(new Node(nx, ny));
                    visited[nx][ny] = group_num;
                } 
            }
        }
        group_amount.add(group_cnt);
    }
    
    public int solution(int[][] land) {
        int answer = 0;
        n = land.length;
        m = land[0].length;
        
        // visited 초기화 
        int[][] visited = new int[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                visited[i][j] = -1;
            }
        }
        
        // bfs
        int group_num = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++) {
                if (land[i][j] == 1 && visited[i][j] == -1) {
                    bfs(i, j, land, visited, group_num);
                    group_num += 1;
                } 
            }
        }
        
        // col_group 초기화
        for(int col=0; col<m; col++) {
            col_groups.put(col, new HashSet<Integer>());   
        }
        
        for(int col=0; col<m; col++) {
            for(int row=0; row<n; row++) {
                if (land[row][col] == 0) continue;
                if (!col_groups.get(col).contains(visited[row][col])) {
                    col_groups.get(col).add(visited[row][col]);
                }
            }
        }
        
        int[] col_sum = new int[m];
        for(int col=0; col<m; col++) {
            int _sum = 0;
            for (Integer gn : col_groups.get(col)) {
                _sum += group_amount.get(gn);
            }
            col_sum[col] = _sum;
            if (_sum > answer) {
                answer = _sum;
            }
        }
        return answer;
    }
}