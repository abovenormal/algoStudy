import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static class Lecture implements Comparable<Lecture> {
        int no, start, end;

        public Lecture(int no, int start, int end) {
            this.no = no;
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Lecture o) {
            return this.start - o.start;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        PriorityQueue<Lecture> lectures = new PriorityQueue<>();

        //입력받기
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int no = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            lectures.add(new Lecture(no, start, end));
        }

        //종료시간을 기준으로 하는 방을 정렬
        PriorityQueue<Integer> rooms = new PriorityQueue<>();
        rooms.add(lectures.poll().end);

        while(!lectures.isEmpty()) {
            int roomsCnt = rooms.size();
            Lecture curLecture = lectures.poll();
            boolean isPossible = false;

            for(int i = 0; i < roomsCnt; i++) {
                //강의하고 있는 강의실에서 강의를 할 수 있다면
                if(rooms.peek() <= curLecture.start ) {
                    rooms.poll();   //현재 강의실에서의 강의를 제거
                    rooms.add(curLecture.end);  //다음 강의의 종료시간 넣기
                    isPossible = true;
                    break;
                }
            }
            if(!isPossible) rooms.add(curLecture.end);
        }

        System.out.println(rooms.size());

    }   //main 함수 끝
}