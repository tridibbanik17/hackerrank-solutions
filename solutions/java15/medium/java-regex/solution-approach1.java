// ──────────────────────────────────────────────────
// Problem     Java Regex
// Difficulty  Medium
// Subdomain   Strings
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-06-21, 10:37 p.m.
// ──────────────────────────────────────────────────

import java.io.*;
import java.util.*;

class MyRegex {
    String pattern = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$";
}


public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        MyRegex r = new MyRegex();
        while (sc.hasNextLine()) {
            System.out.println(sc.nextLine().matches(r.pattern));
        }
    }
}


