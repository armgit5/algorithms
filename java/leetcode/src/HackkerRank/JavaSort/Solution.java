package HackkerRank.JavaSort;

import java.io.File;
import java.io.IOException;
import java.util.*;

class Student{
    private int id;
    private String fname;
    private double cgpa;
    public Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }
    public int getId() {
        return id;
    }
    public String getFname() {
        return fname;
    }
    public double getCgpa() {
        return cgpa;
    }
}

//Complete the code
public class Solution
{
    public static void main(String[] args) throws IOException {
//        Scanner in = new Scanner(System.in);
        Scanner in = new Scanner(new File ("leetcode/src/HackkerRank/JavaSort/input.txt"));
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<>();
        while(testCases>0){
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            Student st = new Student(id, fname, cgpa);
            studentList.add(st);

            testCases--;
        }

        Collections.sort(studentList, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                if (o1.getCgpa() == o2.getCgpa()) {
                    return o1.getFname().compareTo(o2.getFname());
                }
                return o2.getCgpa() > o1.getCgpa() ? 1 : -1;
            }
        });

        for(Student st: studentList){
            System.out.println(st.getFname());
        }
    }
}