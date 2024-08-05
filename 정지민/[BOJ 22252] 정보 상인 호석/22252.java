import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int q = Integer.parseInt(br.readLine());
        HashMap<String, PriorityQueue<Integer>> map = new HashMap<>();
        long answer = 0;

        for (int i=0; i<q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            
            int command = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            
            if (command == 1) {
                int k = Integer.parseInt(st.nextToken());

                if (map.containsKey(name)) {
                    for(int j=0; j<k; j++) {
                        map.get(name).add(Integer.parseInt(st.nextToken()));
                    }
                }
                else {
                    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
                    for(int j=0; j<k; j++) {
                        pq.add(Integer.parseInt(st.nextToken()));
                    }
                    map.put(name, pq);
                }
            }
            else {
                int b = Integer.parseInt(st.nextToken());

                if (map.containsKey(name)) {
                    if (b <= map.get(name).size()) {
                        for(int j=0; j<b; j++) {
                            answer += (int) map.get(name).poll();
                        }
                    }
                    else {
                        answer += map.get(name).stream().mapToInt(Integer::intValue).sum();
                        map.get(name).clear();
                    }
                }
            }
        }

        System.out.println(answer);
    }
}