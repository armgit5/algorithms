// https://www.youtube.com/watch?v=OOtD38U5VWk&list=PLNmW52ef0uwsjnM06LweaYEZr-wjPKBnj&index=26

package ByteByByte.Intersect;

public class Line {

    private static double epsilon = 0.0001;
    private double slope;
    private double yIntercept;

    // Initialize Instance
    public Line(double slope, double yIntercept) {
        this.slope = slope;
        this.yIntercept = yIntercept;
    }

    public boolean intercept(Line line) {
        // Check for the same lines
        if (this.sameLine(line)) return true;
        // If not the same line, but slopes are more than epsilon
        if (Math.abs(this.slope - line.slope) > epsilon) return true;
        return false;
    }

    // Check if 2 Lines are the same line
    private boolean sameLine(Line line) {
        return Math.abs(this.slope - line.slope) < epsilon &&
                Math.abs(this.yIntercept - line.yIntercept) < epsilon;
    }

    public static void main(String[] args) {

        Line a = new Line(0,1);
        Line b = new Line(1,1);
        Line c = new Line(0, 2);
        Line d = new Line(0, 2);

        System.out.println(a.intercept(b));
        System.out.println(a.intercept(c));
        System.out.println(c.intercept(d));
    }
}
