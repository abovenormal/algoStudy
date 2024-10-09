import java.util.*;

class Solution {

    static List<ArrayList<Integer>> permus = new ArrayList<ArrayList<Integer>>();
    
    public void permutations(int[] arr, int[] output, boolean[] visited, int depth, int r) {
        if (depth == r) {
            ArrayList<Integer> adding = new ArrayList<>();
            for (int out : output) {
                adding.add(out);
            }
            permus.add(adding);
            return;
        }
        
        for(int i=0; i<arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = arr[i];
                permutations(arr, output, visited, depth+1, r);
                visited[i] = false;
            }
        } 
    }
    
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        int n = dungeons.length;
        
        int[] temp = new int[n];
        for(int i=0; i<n; i++) {
            temp[i] = i;
        }
        permutations(temp, new int[n], new boolean[n], 0, n);
        
        for(int i=0; i<permus.size(); i++) {
            int cur_k = k;
            int cnt = 0;
            // permus[i] 의 순서대로 던전을 방문한다.
            for(int d_idx : permus.get(i)) {
                if (cur_k >= dungeons[d_idx][0]) {
                    cnt += 1;
                    cur_k -= dungeons[d_idx][1];
                } 
            }
            answer = Math.max(answer, cnt);
        }
        return answer;
    }
}