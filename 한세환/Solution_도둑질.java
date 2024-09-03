public class Solution {

    public static int solution(int[] money) {
        int answer = 0;
        int[] dpO = new int[money.length]; //첫집, 짝수
        int[] dpX = new int[money.length]; //막집, 홀수
        int len = money.length;

        dpO[0] = money[0];
        dpO[1] = 0;
        dpO[2] = dpO[0] + money[2];

        dpX[0] = 0;
        dpX[1] = money[1];
        dpX[2] = money[2];

        for (int i = 3; i < len - 1; i++) {
            dpO[i] = money[i] + Math.max(dpO[i - 2], dpO[i - 3]);
            dpX[i] = money[i] + Math.max(dpX[i - 2], dpX[i - 3]);
        }
        dpX[len - 1] = money[len - 1] + Math.max(dpX[len - 3], dpX[len - 4]);

        int first = Math.max(dpO[len - 2], dpO[len - 3]);
        int second = Math.max(dpX[len - 1], dpX[len - 2]);
        answer = Math.max(first, second);
        return answer;
    }


    public static void main(String[] args) {
        int money[] = {1, 2, 3, 1};
        System.out.println(solution(money));
    }
}