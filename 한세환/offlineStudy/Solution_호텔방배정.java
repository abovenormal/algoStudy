import java.util.*;

/*
* 프로그래머스 : 호텔 방 배정 (Lv.4)
* 카카오 인턴쉽 (2019)
* HashMap을 활용한 재귀
* */

public class Solution {

    static HashMap<Long,Long> roomMap;
    static long roomSize;
    public static long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        roomMap = new HashMap<>();
        roomSize = k;

        for(int i=0;i<room_number.length;i++){
            answer[i] = findRoom(room_number[i]);
        }

        for (long l : answer){
            System.out.println(l);
        }
        return answer;
    }

    public static long findRoom(long roomNumber){

        if(!roomMap.containsKey(roomNumber)){
            roomMap.put(roomNumber,(roomNumber+1)%roomSize);
            return roomNumber;
        }
        long emptyRoom = findRoom(roomMap.get(roomNumber));
        roomMap.put(roomNumber,(emptyRoom+1)%roomSize);
        return emptyRoom;
    }


    public static void main(String[] args) {

        solution(10, new long[]{1, 3, 4, 1, 3, 1});
    }
}
