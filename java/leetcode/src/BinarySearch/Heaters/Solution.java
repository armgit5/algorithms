package BinarySearch.Heaters;

import java.util.Arrays;

/**
 * Created by arm on 7/26/2017 AD.
 */
public class Solution {

    public int findRadius(int[] houses, int[] heaters) {

        Arrays.sort(heaters);
        int result = Integer.MIN_VALUE;

        for (int house: houses) {
            int index = Arrays.binarySearch(heaters, house);

            if (index < 0) {
                index = -(index + 1);
            }
            int heaterToRightHouse = index - 1 >= 0 ? house - heaters[index - 1] : Integer.MAX_VALUE;
            int heaterToLeftHouse = index < heaters.length ? heaters[index] - house: Integer.MAX_VALUE;
            int minDis = Math.min(heaterToLeftHouse, heaterToRightHouse);
            result = Math.max(result, minDis);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] houses = {1, 2, 3, 4, 5, 6, 7};
        int[] heaters = {2, 5, 6};

//        int[] houses = {1, 2, 3};
//        int[] heaters = {2};

        Solution s = new Solution();
        System.out.println(s.findRadius(houses, heaters));



    }
}
