package com.szymczak.task1;

/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5,
 *  we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
public class Problem1 {
    private static int getSumOfNumbersDividedBy3Or5(int n) {
        int counter = 0;
        while (--n > 0) {
            if (n % 3 == 0 || n % 5 == 0) {
                counter += n;
            }
        }
        return counter;
    }

    public static void main(String[] args) {
        System.out.printf("Sum of all numbers is: %d", getSumOfNumbersDividedBy3Or5(1000));
    }
}
