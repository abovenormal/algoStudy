/* 1. hashCode(), equals() 함수 기억하기
 * 2. 조합 구현 코드 기억하기
 */

import java.io.*;
import java.util.*;

class Main {

    static class Node {
        int x;
        int y;
    
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return x == node.x && y == node.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x,y);
        }
    }

    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,-1,0,1};

    static char[][] _map = new char[5][5];
    static int n = 5;

    static int answer = 0;
    static ArrayList<Node> pos = new ArrayList<>();

    static int count_Y(List<Node> arr) {
        int cnt = 0;
        for (Node node : arr) {
            if (_map[node.x][node.y] == 'Y') {
                cnt += 1;
            }
        }
        return cnt;
    }

    // arr 에 들어있는 노드들이 어느 한 노드에서 시작해서 bfs 로 모두 방문 가능한지 체크
    static boolean bfs(List<Node> arr) {
        Queue<Node> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];
        q.add(arr.get(0));
        visited[arr.get(0).x][arr.get(0).y] = true;

        while (!q.isEmpty()) {
            Node cur = q.poll();

            for(int i=0; i<4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if (nx<0 || nx>=n || ny<0 || ny>=n) continue;

                Node next = new Node(nx, ny);

                if (!arr.contains(next)) continue;

                if (visited[nx][ny] == false) {
                    visited[nx][ny] = true;
                    q.add(next);
                }
            }
        }

        // arr 의 노드들이 모두 visited = true 상태가 아니라면, false 리턴
        for(Node node : arr) {
            if (visited[node.x][node.y] == false){
                return false;
            }
        }
        return true;
    }

    public static void combinations(List<Node> arr, List<Node> output, int startIdx, int depth, int r) {
        // 7명 중 S 가 4명 이상이여야 -> Y 가 4명 이상이면 조건 불충족이므로 백트랙
        if (output.size() >= 4 && count_Y(output) >= 4) {
            return;
        }

        // 종료조건
        if (depth == r) {
            if (bfs(output) == false) {     // 7명이 가로나 세로로 인접하지 않다면, 조건 불충족
                return;
            }
            answer += 1;
            return;
        }

        for (int i=startIdx; i<arr.size(); i++) {
            output.add(arr.get(i));
            combinations(arr, output, i+1, depth+1, r);
            output.remove(arr.get(i));
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i=0; i<n; i++) {
            String _input = br.readLine();
            for (int j=0; j<n; j++) {
                _map[i][j] = _input.charAt(j);
                pos.add(new Node(i,j));
            }
        }   

        combinations(pos, new ArrayList<Node>(), 0, 0, 7);
  
        System.out.println(answer);
    }
}
