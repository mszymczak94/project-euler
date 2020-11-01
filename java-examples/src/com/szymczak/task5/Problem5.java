package com.szymczak.task5;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
 2520 is the smallest number that can be divided by each of the numbers
 from 1 to 10 without any remainder.
 What is the smallest positive number that is evenly divisible by all of
 the numbers from 1 to 20?
*/
public class Problem5 {
    public static void main(String[] args) {
        System.out.printf("Smallest number divided by all values to n is: %d\n", getSmallestNumberDividedByAll(20));
    }

    private static long getSmallestNumberDividedByAll(int i) {
        long tempI = i;
        int startPosition = i < 6 ? 1 : 6;
        List<Integer> numbersToCheck = IntStream
                .rangeClosed(startPosition, i)
                .boxed()
                .collect(Collectors.toList());
        System.out.println(numbersToCheck);

        while (true) {
            if (isDividedByAll(numbersToCheck, tempI)) {
                return tempI;
            }
            tempI += i;
        }
    }

    private static boolean isDividedByAll(List<Integer> numbersToCheck, long tempI) {
        for (Integer integer : numbersToCheck) {
            if (tempI % integer != 0) {
                return false;
            }
        }
        return true;
    }
}
