/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   main.cpp
 * Author: asuwansiri
 *
 * Created on October 28, 2017, 8:22 PM
 */

#include <cstdlib>
#include <vector>
#include <iostream>

using namespace std;

/*
 *
 */

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size()-2;
        while (i>=0 && nums[i] > nums[i+1]) {
            i--;
        }

        if (i >= 0) {
            int j = nums.size()-1;
            while (j>=0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin()+i+1, nums.end());
    }

private:

};

int main(int argc, char** argv) {


    int numsArr[] = {1,5,8,4,7,6,5,3,1};
    vector<int>::iterator it;
    vector<int> nums;

    for (int num : numsArr) {
        nums.push_back(num);
    }

    Solution s;
    s.nextPermutation(nums);

    for (it = nums.begin(); it != nums.end(); ++it) {
        cout << *it << " ";
    }


    return 0;
}

