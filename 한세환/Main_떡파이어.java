import java.io.*;
import java.util.*;

public class Main {

    static long rest = 1000000007;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Long n = Long.parseLong(br.readLine());
        int sum = 1;

        if(n==0)
            System.out.println(1);
        else{
            mod(2,n);
        }
    }

    public static void mod (long a , long n){
        long sum = 1;

        while(n>0){
            if(n%2==1){
                sum = sum*a%rest;
                a = a*a%rest;
                sum /=2;
            }
        }
        System.out.println(sum);
    }
}