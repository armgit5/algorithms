package DesignPatterns.Singleton;

public class Singleton {

    private static int counter = 0;
    private static Singleton instance = null;
    public static Singleton GetInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    public void printDetail(String message) {
        System.out.println(message);
    }

    public static void main(String[] args) {
        Singleton employee = Singleton.GetInstance();
        employee.printDetail("employee");

        Singleton student = Singleton.GetInstance();
        student.printDetail("student");
    }
}
