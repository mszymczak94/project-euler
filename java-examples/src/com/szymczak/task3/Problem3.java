package com.szymczak.task3;

import static com.szymczak.utils.Utils.isPrime;

public class Problem3 {
    public static void main(String[] args) {
        System.out.printf("Largest biggest prime is: %d", getLargestPrimeFactor(600851475143L));
    }

    private static long getLargestPrimeFactor(long n) {
        long biggestPrime = -1;
        long primeToDive = 2;
        while (primeToDive <=n) {
            if (n % primeToDive == 0) {
                n /= primeToDive;
                if (primeToDive > biggestPrime) {
                    biggestPrime = primeToDive;
                }
                primeToDive = 2;
            } else {
                while (true) {
                    if (isPrime(++primeToDive)) break;
                }
            }
        }
        return biggestPrime;
    }
}
