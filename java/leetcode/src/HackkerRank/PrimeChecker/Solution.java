package HackkerRank.PrimeChecker;

import java.io.BufferedReader;
import java.io.FileReader;
import java.lang.reflect.Method;
import java.math.BigInteger;
import java.util.HashSet;
import java.util.Set;

class Prime {

    private int isPrime(int num) {
        boolean isPrime = true;
        int temp;
        if (num < 2) return -1;
        for (int i = 2; i <= num/2; i++) {
            if (num % 2 == 0) {
                temp=num%i;
                if(temp==0)
                {
                    isPrime=false;
                    return -1;
                }
            }
        }
        return num;
    }

    public void checkPrime(int... intArgs) {

        String sep = "";
        for (int i:
             intArgs) {
//            System.out.println(i);
            if ((BigInteger.valueOf(i).isProbablePrime(1))) {
                System.out.print(sep + i);
                sep = " ";
            }
        }
        System.out.println("");
    }
}

public class Solution {

    public static void main(String[] args) {
        try{
            FileReader file = new FileReader("leetcode/src/HackkerRank/PrimeChecker/input.txt");
            BufferedReader br=new BufferedReader(file);
            int n1=Integer.parseInt(br.readLine());
            int n2=Integer.parseInt(br.readLine());
            int n3=Integer.parseInt(br.readLine());
            int n4=Integer.parseInt(br.readLine());
            int n5=Integer.parseInt(br.readLine());
            Prime ob=new Prime();
            ob.checkPrime(n1);
            ob.checkPrime(n1,n2);
            ob.checkPrime(n1,n2,n3);
            ob.checkPrime(n1,n2,n3,n4,n5);
            Method[] methods=Prime.class.getDeclaredMethods();
            Set<String> set=new HashSet<>();
            boolean overload=false;
            for(int i=0;i<methods.length;i++)
            {
                if(set.contains(methods[i].getName()))
                {
                    overload=true;
                    break;
                }
                set.add(methods[i].getName());

            }
            if(overload)
            {
                throw new Exception("Overloading not allowed");
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }

}
