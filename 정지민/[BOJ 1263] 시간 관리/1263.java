import java.util.*;
import java.io.*;

class Main {

    static class Task {
        int s;
        int t;

        public Task(int s, int t) {
            this.s = s;
            this.t = t;
        }
    }

    static int n;
    static Task[] tasks;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        tasks = new Task[n];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            tasks[i] = new Task(s, t);
        }

        Arrays.sort(tasks, (o1, o2) -> Integer.compare(o2.s, o1.s));

        int time = tasks[0].s;
        for(int i=0; i<n; i++) {
            int limit_time = tasks[i].s;
            int duration = tasks[i].t;

            if (limit_time >= time) {
                time -= duration;
            } else {
                time = limit_time - duration;
            }

            if (time < 0) {
                System.out.println(-1);
                return;
            }
        }

        System.out.println(time);
    }
}