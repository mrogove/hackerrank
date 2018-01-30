/*****************
https://www.hackerrank.com/challenges/30-interfaces/problem
Take an int, and return sum of all divisors.
Python has multiple inheritance and therefore doesn't use interfaces like this.
To stick with continuity of the challenge I've switched to Java.
******************/
import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}
//Write your code here

class Calculator implements AdvancedArithmetic{ //defined in given code
    public int divisorSum(int n){ //name defined in given code
       int sum = 0;
       for(int i = 1; i <= n; i++) {
           if(n%i==0){
               sum = sum + i;
           }
       }
       return sum;
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

      	AdvancedArithmetic myCalculator = new Calculator();
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
