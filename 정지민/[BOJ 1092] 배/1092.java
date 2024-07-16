/* 1트 => 제출 시 틀림
 * [ 반례 ]
 *  2
 *  1 2
 *  4
 *  1 1 2 2
 *  - 답: 2 / 결과: 3
 *  
 *  [ 틀린 이유 ]
 *  - 박스들을 순서대로 정렬한뒤 앞에서부터 크레인 개수만큼 끊어서 담을 수 있는지 체크했기 때문에,
 *     (1 담기 -> 1,2 담기 -> 2담기)  << 이렇게 담게 되서 틀림.
 */
// import java.util.*;
// import java.io.*;

// class Main {

//     static int n;
//     static int[] crain;
//     static int m;
//     static int[] box;
//     static int answer = 0;

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         n = Integer.parseInt(br.readLine());
//         crain = new int[n];
//         StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//         for (int i=0; i<n; i++) {
//             crain[i] = Integer.parseInt(st.nextToken());
//         }
//         m = Integer.parseInt(br.readLine());
//         box = new int[m];
//         st = new StringTokenizer(br.readLine(), " ");
//         for (int i=0; i<m; i++) {
//             box[i] = Integer.parseInt(st.nextToken());
//         }

//         Arrays.sort(crain);
//         Arrays.sort(box);

//         int turn = 1;
//         int box_idx = 0;
       
//         for(turn = 1; turn <= box.length; turn++) {
//             // 크레인 순회하며 각 크레인으로 몇번째 박스까지 가능한지 체크
//             for(int i=0; i<crain.length; i++) {
//                 if (box[box_idx] <= crain[i]) {
//                     box_idx += 1;
//                 }
//                 if (box_idx == box.length) break;  
//             }
//             if (box_idx == box.length) break;  
//         }

//         if (box_idx != box.length) {
//             System.out.println(-1);
//         }
//         else {
//             System.out.println(turn);
//         }
//     }
// }



/* 2트
 */
import java.util.*;
import java.io.*;
 
class Main {

    static int n;
    static List<Integer> crain = new ArrayList<Integer>();
    static int m;
    static List<Integer> box = new ArrayList<Integer>();
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i=0; i<n; i++) {
            crain.add(Integer.parseInt(st.nextToken()));
        }
        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        for (int i=0; i<m; i++) {
            box.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(crain);
        Collections.sort(box);

        crain.sort(Collections.reverseOrder());
        box.sort(Collections.reverseOrder());

        if (crain.get(0) < box.get(0)) {
            System.out.println(-1);
            return;
        }

        int day = 0;
        while (!box.isEmpty()) {
            // 하루에 옮길 수 있는 박스들 옮기기
            int boxIdx = 0, crainIdx = 0;

            while (crainIdx < n) {
                if (boxIdx == box.size())
                    break;
                else if (crain.get(crainIdx) >= box.get(boxIdx)) {   // 옮길 수 있는 박스 찾으면, 해당 크레인으로 옮기고, 다음 크레인 사용하기
                    box.remove(boxIdx);
                    crainIdx += 1;
                }
                else {              // 옮길 수 있는 박스 못찾으면, 더 작은 무게의 박스 탐색하기
                    boxIdx += 1;
                }
            }

            day += 1;
        }
        
        System.out.println(day);     
    }
}