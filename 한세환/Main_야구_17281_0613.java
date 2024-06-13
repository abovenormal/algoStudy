/*
* 백준 17281
* 브루트포스(순열) 활용.
*
* */
import java.io.*;
import java.util.*;

public class Main {

    static int innings, max;
    static int[][] grid;
    static boolean[] visit, base;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        innings = Integer.parseInt(br.readLine());

        grid = new int[innings][9];

        for (int i = 0; i < innings; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        max = 0;
        visit = new boolean[9];
        arr = new int[9];
        base = new boolean[3];
        visit[3] = true;
        arr[3] = 0;
        permutation(1);

        System.out.println(max);
    }

    public static void permutation(int pNum){

        if (pNum == 9) {
            int score = simulation();
            max = Math.max(score, max);
            return;
        }
        for(int i=0;i<9;i++){
            if(visit[i]) continue;

            visit[i] = true;
            arr[i] = pNum;
            permutation(pNum+1);
            visit[i] = false;
        }
    }

    public static int simulation(){
        int score = 0;
        int playerIndex = 0;

        for (int i = 0; i < innings; ++i) {
            base[0] = false;
            base[1] = false;
            base[2] = false;

            int outCount = 0; // 이닝의 시작에는 아웃카운트가 0이다.
            while (outCount < 3) {
                int curPlayer = arr[playerIndex];
                playerIndex = (playerIndex + 1) % 9; // 다음 타자 번호 수정

                int act = grid[i][curPlayer];
                if (act == 0)
                    outCount++;
                else
                    score += movePlayer(act);
            }
        }
        return score;
    }

    private static int movePlayer(int act) {
        int score = 0;
        // 타자 주자를 움직인다.
        if (act == 4) {
            // 홈런인경우
            for (int i = 0; i < 3; ++i)
                if (base[i]) { // 주자가 있다면 홈런 점수에 1점씩 추가된다.
                    base[i] = false;
                    score++;
                }
            score++; // 타자 주자의 점수도 더해야한다.
        } else {
            // 존재하는 주자를 모두 이동시켜본다.
            for (int i = 0; i < act; ++i) {
                if (base[2]) { // 3루 주자가 이동
                    base[2] = false;
                    score++;
                }

                if (base[1]) { // 2루 주자가 이동
                    base[1] = false;
                    base[2] = true;
                }

                if (base[0]) { // 1루 주자가 이동
                    base[0] = false;
                    base[1] = true;
                }
            }
            // 타자 주자를 움직인다.
            base[act - 1] = true;
        }
        return score;
    }
}

