import java.util.*;

// 프로그래머스 코드챌린지 2025 - 비밀코드 해독
class Solution {

    static int[][] qq;
    static int[] ans1;
    static boolean visited[];
    static int cnt = 0;

    public static int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        qq = q;
        ans1 = ans;
        visited = new boolean[n + 1];

        comb(0, 1);

        cnt = answer;
        return cnt;
    }

    public static void comb(int depth, int start) {
        if (depth == 5) {
            List<Integer> list = new ArrayList<>();

            for (int i = 0; i < visited.length; i++) {
                if (visited[i]) {
                    list.add(i);
                }
            }
            check(list);
            return;
        } else {
            for (int i = start; i < visited.length; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    comb(depth + 1, i + 1);
                    visited[i] = false;
                }
            }

        }
    }

    public static void check(List<Integer> list) {

        for (int i : list) {
            System.out.print(i + " ");
        }

        boolean check = true;
        for (int i = 0; i < qq.length; i++) {
            int curA = 0;
            for (int j = 0; j < 5; j++) {
                if (list.contains(qq[i][j])) {
                    curA++;
                }
            }

            if (ans1[i] != curA) {
                check = false;
                break;
            }
        }

        if (check) {
            cnt++;
        }
        System.out.println(cnt);
    }


    public static void main(String[] args) {

        System.out.println(solution(10, new int[][]{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {3, 7, 8, 9, 10}, {2, 5, 7, 9, 10}, {3, 4, 5, 6, 7}}, new int[]{2, 3, 4, 3, 3}));
        System.out.println(solution(15, new int[][]{{2, 3, 9, 12, 13},
                {1, 4, 6, 7, 9},
                {1, 2, 8, 10, 12},
                {6, 7, 11, 13, 15},
                {1, 4, 10, 11, 14}}, new int[]{2, 1, 3, 0, 1}));

    }
}