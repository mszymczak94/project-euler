package com.szymczak.task4;

import static com.szymczak.utils.Utils.isPalindrome;

/*
 * A palindromic number reads the same both ways.
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public class Problem4 {
    public static int getBiggestPalindrome() {
        int biggestPalindrome = -1;
        for (int i = 999; (i * i) > biggestPalindrome; i--) {
            for (int j = i; j > 100; j--) {
                int result = j * i;
                if (isPalindrome(Integer.toString(result)) && biggestPalindrome < result) {
                    biggestPalindrome = result;
                    break;
                }
            }
        }
        return biggestPalindrome;
    }

    public static void main(String[] args) {
        System.out.printf("Largest palindrome made from product of two 3-digit numbers is: %d", getBiggestPalindrome());
    }
}
