import java.io.*;
import java.util.*;

class Jewelry {
    int weight;
    int val;

    Jewelry(int weight, int val) {
        this.weight = weight;
        this.val = val;
    }
}

public class Main {
    static int n, k;
    static long max_kilo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        Jewelry[] jewelries = new Jewelry[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int weight = Integer.parseInt(st.nextToken());
            int val = Integer.parseInt(st.nextToken());
            jewelries[i] = new Jewelry(weight, val);
        }

        Arrays.sort(jewelries, new Comparator<Jewelry>() {
            @Override
            public int compare(Jewelry o1, Jewelry o2) {
                if (o1.weight == o2.weight) {
                    return o2.val - o1.val;
                }
                return o1.weight - o2.weight;
            }
        });

        int[] bags = new int[k];


        for (int i = 0; i < k; i++) {
            bags[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(bags);

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        for (int i = 0, j = 0; i < k; i++) {
            while (j < n && jewelries[j].weight <= bags[i]) {

                //System.out.println(i+" "+jewelries[j].val + " "+ bags[i]);
                pq.offer(jewelries[j++].val);

            }

            if (!pq.isEmpty()) {
                max_kilo += pq.poll();
            }
        }

        System.out.println(max_kilo);
    }
}
