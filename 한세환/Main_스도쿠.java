import java.io.*;
import java.util.*;

class Node {
    int x, y;

    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}


public class Main {
    static int[][] map = new int[9][9];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < 9; j++) {
                int temp = Integer.parseInt(st.nextToken());
                map[i][j] = temp;
            }
        }

        bt(0, 0);
    }

    public static void bt(int r, int c) {
        if (c == 9) {
            bt(r + 1, 0);
            return;
        }
        if (r == 9) {
            print();
            System.exit(0);
            return;
        }

        if (map[r][c] == 0) {
            for (int i = 1; i <= 9; i++) {
                if (check(r, c, i)) {
                    map[r][c] = i;
                    bt(r, c + 1);
                }
            }
            map[r][c] = 0;
            return;
        }

        bt(r, c + 1);
    }

    public static boolean check(int r, int c, int val) {

        for (int i = 0; i < 9; i++) {
            if (map[r][i] == val) {
                return false;
            }
        }

        for (int i = 0; i < 9; i++) {
            if (map[i][c] == val) {
                return false;
            }
        }

        int setR = (r / 3) * 3;
        int setC = (c / 3) * 3;

        for (int i = setR; i < setR + 3; i++) {
            for (int j = setC; j < setC + 3; j++) {
                if(map[i][j]== val)
                    return false;
            }
        }

        return true;
    }


    public static void print() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }
}