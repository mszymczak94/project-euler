package com.szymczak.task6;

import java.util.stream.LongStream;

/*
    Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
*/
public class Problem6 {
    public static void main(String[] args) {
        System.out.printf("Sum of n natural numbers and square of the sum is %d", getResult(100));
    }

    private static long getResult(int n) {
        long sum = LongStream.rangeClosed(1, n)
                .map(value -> value * value)
                .sum();
        long sumOfNNaturalNumbersWithSquare = (long) Math.pow(LongStream.rangeClosed(1, n)
                .sum(), 2);
        return sumOfNNaturalNumbersWithSquare - sum;
    }
}
