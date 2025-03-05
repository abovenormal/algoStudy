import java.util.*;

class Solution {
    Queue<Integer> queue = new LinkedList<>();
    List<Integer> list = new LinkedList<>();

    public int solution(int[] priorities, int location) {
        int answer = 0;

        for(int i=0;i<priorities.length;i++){
            queue.add(i);
            list.add(priorities[i]);
        }

        Collections.sort(list);

        while(true){

            int temp = queue.poll();

            if(priorities[temp] == list.get(list.size()-1)){
                answer++;
                list.remove(list.get(list.size()-1));
                if(temp==location){
                    break;
                }
            }else{
                queue.add(temp);
            }

        }

        return answer;
    }
}