/* 1트 => 실패.
[ 원인 ]
- java 의 Arrays.binarySearch() 함수는 특정 값 x 를 찾고자 하는데 x 가 배열에 여러 개 있을때, 가장 앞쪽 인덱스를 반환하지 않는다.
    - 어떤 값이 반환될지 모름!
    - 파이썬의 bisect_left 와의 차이점!!
*/

// import java.util.*;

// class Solution {
    
//     static List<ArrayList<Integer>> combis = new ArrayList<>();
//     static List<ArrayList<Integer>> rolled_idxs = new ArrayList<>();
    
//     public static void combinations(int[] arr, int[] output, int startIdx, int depth, int r) {
//         if (depth == r) {
//             ArrayList<Integer> adding = new ArrayList<>();
//             for (int num : output) {
//                 adding.add(num);
//             }
//             combis.add(adding);
//             return;
//         }
        
//         for(int i=startIdx; i<arr.length; i++) {
//             output[depth] = arr[i];
//             combinations(arr, output, i+1, depth+1, r);
//         }
//     }
    
//     public static void permutation_dupli(int[] arr, int[] output, int depth, int r) {
//         if (depth == r) {
//             ArrayList<Integer> adding = new ArrayList<>();
//             for (int num : output) {
//                 adding.add(num);
//             }
//             rolled_idxs.add(adding);
//             return;
//         }
        
//         for(int i=0; i<arr.length; i++) {
//             output[depth] = arr[i];
//             permutation_dupli(arr, output, depth+1, r);
//         }
//     }
    
//     public int[] solution(int[][] dice) {
        
        
//         int n = dice.length;
//         int[] dice_num = new int[n];
//         for(int i=0; i<n; i++)
//             dice_num[i] = i;
        
//         int[] answer = new int[n/2];
        
//         int[] dice_idx = new int[6];
//         for(int i=0; i<6; i++)
//             dice_idx[i] = i;
        
//         permutation_dupli(dice_idx, new int[n/2], 0, n/2);
        
//         System.out.println("--- rolled_idxs: " + rolled_idxs);
        
//         int max_win_cnt = 0;
//         combinations(dice_num, new int[n/2], 0, 0, n/2);
        
//         for (ArrayList<Integer> a_combi : combis) {
//             // A 가 가지는 주사위
//             int[][] a_dices = new int[n/2][6];
//             for(int i=0; i<n/2; i++) {
//                 a_dices[i] = dice[a_combi.get(i)];
//             }
            
//             // A 가 가지는 주사위로 만들 수 있는 주사위 합
//             int[] a_sums = new int[rolled_idxs.size()];
//             for(int i=0; i<rolled_idxs.size(); i++) {
//                 ArrayList<Integer> rolled = rolled_idxs.get(i);
//                 for(int j=0; j<rolled.size(); j++) {
//                     a_sums[i] += a_dices[j][rolled.get(j)];
//                 }
//             }
            
//             // B 가 가지는 주사위
//             ArrayList<Integer> b_combi = new ArrayList<>();
//             for(int i=0; i<n; i++) {
//                 if (!a_combi.contains(i)) {
//                     b_combi.add(i);
//                 }
//             }
//             int[][] b_dices = new int[n/2][6];
//             for(int i=0; i<n/2; i++) {
//                 b_dices[i] = dice[b_combi.get(i)];
//             }
            
//             // B 가 가지는 주사위로 만들 수 있는 주사위 합
//             int[] b_sums = new int[rolled_idxs.size()];
//             for(int i=0; i<rolled_idxs.size(); i++) {
//                 ArrayList<Integer> rolled = rolled_idxs.get(i);
//                 for(int j=0; j<rolled.size(); j++) {
//                     b_sums[i] += b_dices[j][rolled.get(j)];
//                 }
//             }
            
//             Arrays.sort(b_sums);
            
//             for(int a_sum : a_sums) {
//                 int res = Arrays.binarySearch(b_sums, a_sum);
//                 int cnt = res;
//                 if (res < 0) {
//                     cnt = -res - 1;
//                 }
//                 if (cnt > max_win_cnt) {
//                     max_win_cnt = cnt;
//                     for(int i=0; i<n/2; i++)
//                         answer[i] = a_combi.get(i) + 1;
//                 }
//             }
//         }
//         return answer;
//     }
// }



/* 2트
- binarySearch 함수 구현 시, arr[mid] == target 인 경우에도 end = mid-1 을 해주면, arr 에서 가장 앞쪽에 위치한 target 의 인덱스를 찾을 수 있다.
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    
    static List<ArrayList<Integer>> combis = new ArrayList<>();
    static List<ArrayList<Integer>> rolledIdxs = new ArrayList<>();
    
    public static void combinations(int[] arr, int[] output, int startIdx, int depth, int r) {
        if (depth == r) {
            ArrayList<Integer> adding = new ArrayList<>();
            for (int num : output) {
                adding.add(num);
            }
            combis.add(adding);
            return;
        }
        
        for (int i = startIdx; i < arr.length; i++) {
            output[depth] = arr[i];
            combinations(arr, output, i + 1, depth + 1, r);
        }
    }
    
    public static void product(int[] arr, int[] output, int depth, int r) {
        if (depth == r) {
            ArrayList<Integer> adding = new ArrayList<>();
            for (int num : output) {
                adding.add(num);
            }
            rolledIdxs.add(adding);
            return;
        }
        
        for (int i = 0; i < arr.length; i++) {
            output[depth] = arr[i];
            product(arr, output, depth + 1, r);
        }
    }
    
    public int binarySearch(int x, int[] arr) {
        int start = 0;
        int end = arr.length-1;
        
        while (start <= end) {
            int mid = (start + end) / 2;
            
            if (arr[mid] < x) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }
        return start;
    }
    
    public int[] solution(int[][] dice) {
        int n = dice.length;  
        int[] diceNum = new int[n];
        for (int i = 0; i < n; i++) {
            diceNum[i] = i;
        }
        
        int[] answer = new int[n / 2];
        
        int[] diceIdx = new int[6];
        for (int i = 0; i < 6; i++) {
            diceIdx[i] = i;
        }
        
        product(diceIdx, new int[n / 2], 0, n / 2);
        
        int maxWinCnt = 0;
    
        combinations(diceNum, new int[n / 2], 0, 0, n / 2);
        for (ArrayList<Integer> aCombi : combis) {
            // A의 주사위 조합
            int[][] aDices = new int[n / 2][6];
            for (int i = 0; i < n / 2; i++) {
                aDices[i] = dice[aCombi.get(i)];
            }
            
            // A의 주사위 조합일때 낼 수 있는 모든 점수
            int[] aSums = new int[rolledIdxs.size()];
            for (int i = 0; i < rolledIdxs.size(); i++) {
                ArrayList<Integer> rolled = rolledIdxs.get(i);
                for (int j = 0; j < rolled.size(); j++) {
                    aSums[i] += aDices[j][rolled.get(j)];
                }
            }
            
            // B의 주사위 조합
            ArrayList<Integer> bCombi = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (!aCombi.contains(i)) {
                    bCombi.add(i);
                }
            }
            int[][] bDices = new int[n / 2][6];
            for (int i = 0; i < n / 2; i++) {
                bDices[i] = dice[bCombi.get(i)];
            }
            
            // B의 주사위 조합일때 낼 수 있는 모든 점수
            int[] bSums = new int[rolledIdxs.size()];
            for (int i = 0; i < rolledIdxs.size(); i++) {
                ArrayList<Integer> rolled = rolledIdxs.get(i);
                for (int j = 0; j < rolled.size(); j++) {
                    bSums[i] += bDices[j][rolled.get(j)];
                }
            }
            
            // A의 점수와 B의 점수를 비교하여 A가 이기는 횟수 계산
            Arrays.sort(bSums);
            int a_win_cnt = 0;
            
            for (int aSum : aSums) {
                int win_cnt = binarySearch(aSum, bSums);
                a_win_cnt += win_cnt;
            }
                
            if (a_win_cnt > maxWinCnt) {
                maxWinCnt = a_win_cnt;
                for (int i = 0; i < n / 2; i++) {
                    answer[i] = aCombi.get(i) + 1;
                }
            }
        }
        return answer;
    }
}