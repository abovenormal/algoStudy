import java.io.*;
import java.util.*;

public class Main {

    static class Info {
        int idx, cnt;

        public Info(int idx, int cnt) {
            this.idx = idx;
            this.cnt = cnt;
        }
    }

    static int N, M;
    static ArrayList<Integer> arrayLists[];
    static boolean visit[];
    static int realVisit[]; //실제 지나왔던 경로 저장
    static int start, end, ans;

    public static void main(String[] args) throws IOException {
        input();
        pro();
        System.out.println(ans);
    }

    static void pro() {
        for (int i = 1; i <= N; i++) Collections.sort(arrayLists[i]);

        bfs(start, end);
        for (int i = 1; i <= N; i++) visit[i] = false;

        int last = realVisit[end];
        while (last > 0) {
            visit[last] = true;
            last = realVisit[last];
        }

        bfs(end, start);
    }

    static void bfs(int st, int ed) {
        Queue<Info> q = new ArrayDeque<>();
        q.offer(new Info(st, 0));
        visit[st] = true;

        while (!q.isEmpty()) {
            Info info = q.poll();

            for (int node : arrayLists[info.idx]) {
                if (!visit[node]) {
                    visit[node] = true;
                    realVisit[node] = info.idx;
                    q.offer(new Info(node, info.cnt + 1));
                }

                if (node == ed) {
                    ans += info.cnt + 1;
                    return;
                }
            }
        }
    }

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = parsing(st.nextToken());
        M = parsing(st.nextToken());

        visit = new boolean[N + 1];
        realVisit = new int[N + 1];
        arrayLists = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) arrayLists[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = parsing(st.nextToken());
            int to = parsing(st.nextToken());

            arrayLists[from].add(to);
            arrayLists[to].add(from);
        }

        st = new StringTokenizer(br.readLine());

        start = parsing(st.nextToken());
        end = parsing(st.nextToken());
    }

    static int parsing(String str) {
        return Integer.parseInt(str);
    }
}
