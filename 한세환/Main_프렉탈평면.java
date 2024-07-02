import java.io.*;
import java.util.*;

public class Main {

    static int s, n, k, r1, r2, c1, c2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        s = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        r1 = Integer.parseInt(st.nextToken());
        r2 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        if (s == 0) {
            System.out.println(0);
            return;
        }

        int size = 1;
        while (s-- > 0) {
            size *= n;
        }

        for (int i = r1; i <= r2; i++) {
            for (int j = c1; j <= c2; j++) {
                System.out.print(recursive(size, i, j));
            }
            System.out.println();
        }

    }

    public static int recursive(int size, int x, int y) {

        if (size == 1) return 0;

        int border = size / n;
        if (x >= border * (n - k) / 2 && x < border * (n + k) / 2 && y >= border * (n - k) / 2 && y < border * (n + k) / 2) {
            return 1;
        }

        return recursive(border, x % border, y % border);

    }

}