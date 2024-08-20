import java.io.*;
import java.util.*;

/*
* HashSet과 TreeSet의 차이점
* HashSet : set 인터페이스의 구현 클래스, set의 성질을 그대로 상속 받음. ele의 중복 제거.
* TreeSet : Hashset과 가장 큰 차이는 자동정렬 기능을 해줌. 그렇기에 저장 순서가 유지되지 않고 이진탐색트리 구조로 이루어져
*           추가삭제에는 시간이 조금 더 걸리지만 정렬, 검색에는 높은 성능을 보이는 구조
* */

public class Main {

    static int n;
    static int[] student;
    static boolean[] visited;
    static List<Integer> studentList;
    static List<Integer> pickList;
    static Set<Integer> answer = new TreeSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        student = new int[n + 1];


        for (int i = 1; i < n + 1; i++) {
            student[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 1; i < n + 1; i++) {
            studentList = new LinkedList<>();
            pickList = new LinkedList<>();
            visited = new boolean[n + 1];
            boolean check = true;
            dfs(i);
            Collections.sort(studentList);
            Collections.sort(pickList);

            if (studentList.size() == pickList.size()) {
                for (int j = 0; j < studentList.size(); j++) {
                    if (!studentList.get(j).equals(pickList.get(j))) {
                        check = false;
                    }
                }
            }

            if (check) {
                answer.addAll(studentList);
            }

        }

        System.out.println(answer.size());

        for (int i : answer) {
            System.out.println(i);
        }

    }

    public static void dfs(int x) {
        if (visited[x])
            return;

        visited[x] = true;
        studentList.add(x);
        pickList.add(student[x]);
        dfs(student[x]);
    }
}