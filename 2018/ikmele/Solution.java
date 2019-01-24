//EuzuBillahiminesseydanirracim Bismillahirrahmanirrahim
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s  = new Scanner(System.in);

        long n = s.nextLong();
        long m = s.nextLong();
        long a = s.nextLong();
        long b = s.nextLong();
        long c = s.nextLong();


        if(m % 2 != 0 || a+b < c || a+c < b || c + b < a || Math.abs(a-b) > c || Math.abs(a-c) > b || Math.abs(b-c) > a  ){
            System.out.println("HAYIR");
        }
        else{
            System.out.println("EVET");
        }



    }
}
