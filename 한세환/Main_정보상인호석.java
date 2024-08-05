import java.io.*;
import java.sql.PreparedStatement;
import java.util.*;

public class Main {
    /*
     * 해쉬맵을 이용한 풀이
     * */
//    static int n;
//    static long cost;
//    static HashMap<String, List<Integer>> map = new HashMap<>();
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st;
//
//        n = Integer.parseInt(br.readLine());
//
//        for (int i = 0; i < n; i++) {
//            st = new StringTokenizer(br.readLine());
//            int status = Integer.parseInt(st.nextToken());
//
//            if (status == 1) {
//                add(st);
//            } else if (status == 2) {
//                sell(st);
//            }
//        }
//
//        System.out.println(cost);
//    }
//
//    public static void add(StringTokenizer st) {
//        String name = st.nextToken();
//        int query = Integer.parseInt(st.nextToken());
//        List<Integer> list = new LinkedList<>();
//
//        if (map.containsKey(name)) {
//            list = map.get(name);
//            for (int i = 0; i < query; i++) {
//                list.add(Integer.parseInt(st.nextToken()));
//            }
//        } else {
//            for (int i = 0; i < query; i++) {
//                list.add(Integer.parseInt(st.nextToken()));
//            }
//        }
//        Collections.sort(list, Collections.reverseOrder());
//
//        map.put(name, list);
//    }
//
//    public static void sell(StringTokenizer st) {
//        String name = st.nextToken();
//        int cnt = Integer.parseInt(st.nextToken());
//
//        if (map.containsKey(name)) {
//            List<Integer> curList = map.get(name);
//
//            if (curList.size() <= cnt) {
//                for (int i : curList) {
//                    cost += i;
//                }
//                curList.clear();
//                map.put(name, curList);
//            } else {
//                for (int i = 0; i < cnt; i++) {
//                    cost += curList.get(i);
//                    //System.out.println(cost);
//                }
//                for (int i = 0; i < cnt; i++) {
//                    curList.remove(0);
//                }
//            }
//        }
//    }

    /*
     * PQ를 활용한 풀이
     * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Map<String, PriorityQueue<Integer>> map = new HashMap<>();
        long ans = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int code = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            int cnt = Integer.parseInt(st.nextToken());

            if (code == 1) {
                for(int j =0; j< cnt ;j++){
                    if(!map.containsKey(name)){
                        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
                        pq.add(Integer.parseInt(st.nextToken()));
                        map.put(name,pq);
                    }else{
                        map.get(name).add(Integer.parseInt(st.nextToken()));
                    }
                }
            } else if (code == 2) {
                if(!map.containsKey(name)) continue;
                while(!map.get(name).isEmpty() && cnt>0){
                    ans += map.get(name).poll();
                    cnt--;
                }
            }
        }

        System.out.println(ans);

    }
}