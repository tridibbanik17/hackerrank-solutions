// ──────────────────────────────────────────────────
// Problem     Java Loops II
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    java
// Status      Accepted
// Submitted   2026-05-30, 12:01 a.m.
// ──────────────────────────────────────────────────

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        int prev_sum;
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            prev_sum=a;
            for(int j=0;j<n;j++){
                prev_sum+=(Math.pow(2,j))*b;
                System.out.print(prev_sum+" ");
            }
            System.out.println();
            
        }
        in.close();
    }
}
