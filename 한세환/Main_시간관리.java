import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static Time time[];

    static class Time implements Comparable<Time> {
        int t;
        int s;

        public Time(int t, int s) {
            this.t = t;
            this.s = s;
        }

        @Override
        public int compareTo(Time o) {
            if (o.s == this.s) {
                return Integer.compare(o.t, this.t);
            }
            return Integer.compare(o.s, this.s);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        time = new Time[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());

            time[i] = new Time(t,s);
        }
        Arrays.sort(time);

        int result = time[0].s;
        for(int i=0;i<n;i++){
            if(time[i].s<result)
                result = time[i].s;
            result -= time[i].t;
        }
        if(result<0) System.out.println(-1);
        else System.out.println(result);
    }
}