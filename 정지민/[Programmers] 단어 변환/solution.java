import java.util.*;
import java.io.*;

class Solution {
    
    boolean canGo(String cur, String next) {
        int diff_cnt = 0;
        
        for(int i=0; i<cur.length(); i++) {
            if (cur.charAt(i) != next.charAt(i)) diff_cnt++;
            if (diff_cnt > 1) return false;
        }
        if (diff_cnt == 1)
            return true;
        return false;
    }
    
    int bfs(String start, String end, HashMap<String, ArrayList<String>> graph) {
        Queue<String> q = new LinkedList<>();
        HashMap<String, Integer> visited = new HashMap<>();
        
        q.add(start);
        visited.put(start, 0);
        
        while(!q.isEmpty()) {
            String cur = q.poll();
            
            for (String next : graph.get(cur)) {
                // 아직 방문하지 않았을 경우
                if (!visited.containsKey(next)) {
                    visited.put(next, visited.get(cur) + 1);
                    q.add(next);
                }
                
                // 방문했었지만, 더 작은 횟수로 방문할 수 있는 경우
                else {
                    if (visited.get(next) > visited.get(cur) + 1) {
                        visited.put(next, visited.get(cur) + 1);
                        q.add(next);
                    }
                }
            }
        }
        
        if (!visited.containsKey(end))
            return 0;
        else
            return visited.get(end);
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        // 그래프 초기화
        HashMap<String, ArrayList<String>> graph = new HashMap<>();
        ArrayList<String> begin_g = new ArrayList<>();
        ArrayList<String> target_g = new ArrayList<>();
        for (String word : words) {
            if(canGo(begin, word)) {
                begin_g.add(word);
            }
            if(canGo(target, word)) {
                target_g.add(word);
            }
        }
        graph.put(begin, begin_g);
        graph.put(target, target_g);
        for (String word1 : words) {
            ArrayList<String> word1_g = new ArrayList<>();
            for (String word2 : words) {
                if (canGo(word1, word2)) {
                    word1_g.add(word2);
                }
            }
            graph.put(word1, word1_g);
        }
  
        // bfs
        answer = bfs(begin, target, graph);
        return answer;
    }
}