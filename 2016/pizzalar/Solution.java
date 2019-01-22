//Euzubillahiminesseydanirracim Bismillahirrahmanirrhim
import java.io.*;
import java.util.*;

public class Main {


    public static void Solution(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        ArrayList<Integer> dizi = oku();
        int diziBoyut = dizi.size();

        ArrayList<Integer> ilkBina = new ArrayList();
        int ilkBinaToplamDilim = 0;
        ArrayList<Integer> ikinciBina = new ArrayList(dizi);
        int ikinciBinaToplamDilim = 0;
        int enIyiDurum = -1;
        int enIyiFark = -1;
        int fark;
        for(int i = 0; i<diziBoyut; i++){
            //System.out.println(dizi.size());
            ilkBina.add(dizi.get(i));
            ikinciBina.remove(0);
            ilkBinaToplamDilim += dizi.get(i);
            ikinciBinaToplamDilim = diziToplami(ikinciBina);

            fark = Math.abs(ilkBinaToplamDilim - ikinciBinaToplamDilim);


            if (fark == 0){
                enIyiDurum = i+1;
                enIyiFark = 0;
                break;
            }
            else if(fark < enIyiFark || enIyiFark == -1){
                enIyiDurum = i+1;
                enIyiFark = fark;
            }


        }


        System.out.println(enIyiDurum);

    }

    public static ArrayList<Integer> oku(){
        Scanner s = new Scanner(System.in);
        int r = s.nextInt();
        String data;
        ArrayList<Integer> dizi = new ArrayList();
        s.nextLine();
        for (int i = 0; i<r; i++){
            data = s.nextLine();
            dizi.add(Integer.parseInt(data));
        }
        return dizi;
    }


    public static int diziToplami(ArrayList<Integer> dizi){
        int sonuc = 0;
        for(int i : dizi){
            sonuc += i;
        }
        return sonuc;

    }



}
