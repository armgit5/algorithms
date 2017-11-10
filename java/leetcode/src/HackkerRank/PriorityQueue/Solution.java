package HackkerRank.PriorityQueue;

import java.io.File;
import java.io.IOException;
import java.util.*;

class Student {

    private int id;
    private String name;
    private double cgpa;

    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getID() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getCGPA() {
        return cgpa;
    }

}

class Priorities {

    public List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> pq = new PriorityQueue<>(events.size(), new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                if (o1.getCGPA() == o2.getCGPA()) {
                    if(o1.getName().equals(o2.getName())) {
                        return o1.getID() > o2.getID() ? 1 : -1;
                    }
                    return o1.getName().compareTo(o2.getName());
                }
                return o2.getCGPA() > o1.getCGPA() ? 1 : -1;
            }
        });
        for (String event:
                events) {
            String[] stringList = event.split(" ");
            if (stringList.length > 1) {
                Student student = new Student(Integer.parseInt(stringList[3]), stringList[1], Double.parseDouble(stringList[2]));
                pq.add(student);

            } else {
                pq.poll();
            }
        }

        List<Student> studentList = new ArrayList<>();
        while (!pq.isEmpty()) {
            studentList.add(pq.poll());
        }

        return studentList;
    }
}

public class Solution {

    private final static Priorities priorities = new Priorities();

    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("leetcode/src/HackkerRank/PriorityQueue/input.txt"));
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}
