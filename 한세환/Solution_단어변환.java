import java.io.*;
import java.util.*;
public class Solution {

    static boolean[] visited;
    static int answer;

    public static int solution(String begin, String target, String[] words) {
        boolean checkExist = false;

        visited = new boolean[words.length];

        for(String s : words){
            if(s.equals(target))
                checkExist = true;
        }

        if(!checkExist) return 0;
        dfs(begin, target, words,0);

        return answer;
    }

    public static void dfs(String nextWord, String target, String[] words,int cnt){

        if(nextWord.equals(target)){
            answer = cnt;
            return;
        };

        for(int i =0;i<words.length; i++){
            if(visited[i]) continue;

            int k = 0 ;

            for(int j =0 ; j<nextWord.length() ; j++){
                if(nextWord.charAt(j) == words[i].charAt(j))
                    k++;
            }

            if(k == nextWord.length() -1){
                visited[i] = true;
                dfs(words[i], target, words, cnt+1);
                visited[i] = false;
            }
        }

    }

    public static void main(String[] args) {
    }
}