// ──────────────────────────────────────────────────
// Problem     Java SHA-256
// Difficulty  Medium
// Subdomain   Advanced
// Platform    HackerRank
// Language    java15
// Status      Accepted
// Submitted   2026-06-21, 10:40 p.m.
// Technique   message-digest-hashing
// Time        O(n)
// Space       O(1)
// Trick       Use MessageDigest.getInstance("SHA-256") and format bytes as hex strings using String.format with the %02x specifier to ensure leading zeros.
// Hint        Use %02x to pad single-digit hex values with a zero.
// ──────────────────────────────────────────────────

import java.io.*;
import java.util.*;
import java.security.MessageDigest;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(s.getBytes("UTF-8"));
            
            StringBuilder hex = new StringBuilder();
            for (byte b : hash) {
                hex.append(String.format("%02x", b));
            }
            
            System.out.println(hex.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

