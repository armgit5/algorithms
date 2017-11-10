package IDeserve.Tree;

// 1 3 6
// 2 5 8
// 4 7 9

// http://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/


import java.util.ArrayDeque;
import java.util.Queue;

public class Wuth {

    static void printMatrix(int[][] matrix, int row, int col)
    {
        for (int i=0; i< row; i++)
        {
            for (int j=0; j<col; j++)
                System.out.print(matrix[i][j] + " ");
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        int[] array = {1,2,3,4,5,6,7,8,9};
        Queue<Integer> q = new ArrayDeque<>();

        for (int a: array) {
            q.add(a);
        }

        int[][] m = new int[3][3];

        final int ROW = 3, COL = 3;

        for (int line = 1; line <= (ROW+COL-1); line++) {
            int startRow = line - 1;
            int startCol = Math.max(0, line-ROW);

            int count = Math.min(Math.min(line, (COL-startCol)), ROW);

            for (int i = 0; i < count; i++) {

                if (line > 3) {
                    startRow = 2;
                }

//                System.out.println(startRow-i);
//                System.out.println(startCol+i);
//                System.out.println();
                m[startRow-i][startCol+i] = q.poll();

            }

//            System.out.println("new line");
        }

        printMatrix(m, 3, 3);


    }
}
