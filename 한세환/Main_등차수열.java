import java.io.*;
import java.util.Arrays;

public class Main {

    private static final int MAX_SIZE = 2000;
    private static final int INVALID = -1;
    private static final int INIT = 0;

    private static int n;
    private static int[] arr = new int[MAX_SIZE + 1];
    private static int[][] dp = new int[MAX_SIZE + 1][MAX_SIZE + 1];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        parseInput(br);
        int maxLength = findLongestApLength();
        bw.append(String.valueOf(maxLength));

        br.close();
        bw.close();
    }

    private static void parseInput(BufferedReader br) throws IOException {
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) arr[i + 1] = Integer.parseInt(br.readLine());
        Arrays.sort(arr, 1, n + 1);
    }

    private static int findLongestApLength() {
        int max = 1;
        for (int i = 1; i <= n; i++)
            for (int j = i + 1; j <= n; j++)
                max = Math.max(max, dp(i, j));
        return max;
    }

    private static int dp(int i, int j) {
        if (i > j) return 0;
        else if (i == j) return 1;

        int result = dp[i][j];
        if (result != INIT) return result;

        int target = 2 * arr[j] - arr[i];
        int index = findIndex(target, j + 1);

        if (index == INVALID) return dp[i][j] = 2;
        else return dp[i][j] = dp(j, index) + 1;
    }

    private static int findIndex(int target, int start) {
        int left = start, right = n, mid = (left + right) / 2;
        while (left < right) {
            mid = (left + right) / 2;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        if (left <= n && arr[left] == target) return left;
        if (arr[mid] == target) return mid;
        else return INVALID;
    }
}