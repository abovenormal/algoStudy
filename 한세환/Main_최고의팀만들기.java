import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static int[] white;
    public static int[] black;
    public static int[][][] dp;
    public static void main(String args[]) throws IOException {
        Scanner scan = new Scanner(System.in);
        white = new int[1001];
        black = new int[1001];
        int index = 0;
        while(scan.hasNextInt()){
            white[index] = scan.nextInt();
            black[index] = scan.nextInt();

            index++;
        }
        dp = new int[1001][16][16];
        System.out.println(solution(0, 0, 0, index));

    }
    public static int solution(int i, int wIndex, int bIndex, int N){
        if(wIndex==15 && bIndex==15) return 0;
        if(i==N) return 0;

        if(dp[i][wIndex][bIndex]!=0) return dp[i][wIndex][bIndex];
        //선택 안했을 경우
        int ans = solution(i+1, wIndex, bIndex, N);
        //white
        if(wIndex<15) ans = Math.max(ans, solution(i+1, wIndex+1, bIndex,N)+white[i]);
        if(bIndex<15) ans = Math.max(ans, solution(i+1, wIndex, bIndex+1, N)+black[i]);
        //black
        dp[i][wIndex][bIndex] = ans;
        return dp[i][wIndex][bIndex];
    }
}