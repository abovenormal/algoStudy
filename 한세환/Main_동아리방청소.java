import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] S;
    static int[][][] cache;

    // i번째 날 부터 m번 골라 청소할 때 현재 더러운 정도가 k이면
    // 각 사람들이 느낀 불쾌감의 최소 합
    static int dp(int i, int m, int k) {
        if (i == N) return 0;
        if (cache[i][m][k] != 0) return cache[i][m][k];
        int min = k * S[i] + dp(i + 1, m, k + S[i]);
        if (m > 0) min = Math.min(min, k * S[i] + dp(i + 1, m - 1, 0));
        return cache[i][m][k] = min;
    }

    static void reconstruct(int i, int m, int k, StringBuilder bw) {
        if (i == N) return;
        if (m > 0 && dp(i + 1, m - 1, 0) <= dp(i + 1, m, k + S[i])) {
            bw.append(i + 1).append(" ");
            reconstruct(i + 1, m - 1, 0, bw);
        } else {
            reconstruct(i + 1, m, k + S[i], bw);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder bw = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        S = new int[N];
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) S[i] = Integer.parseInt(st.nextToken());
        cache = new int[N][M + 1][N * 20 + 1];
        bw.append(dp(0, M, 0)).append("\n");
        reconstruct(0, M, 0, bw); bw.append("\n");
        System.out.print(bw);
    }
}