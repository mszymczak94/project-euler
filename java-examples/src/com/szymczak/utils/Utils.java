package com.szymczak.utils;

public class Utils {
    //Primality test using 6k+-1 optimization.
    public static boolean isPrime(long n) {
        if (n <= 3) {
            return n > 1;
        } else if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        int i = 5;
        while (i * i <= n) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
        return true;
    }

    //Check if String is palindrome
    public static boolean isPalindrome(String n) {
        String reversed_n = new StringBuilder(n).reverse().toString();
        return n.equals(reversed_n);
    }
}
