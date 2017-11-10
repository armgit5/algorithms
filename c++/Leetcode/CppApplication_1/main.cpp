/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: asuwansiri
 *
 * Created on October 9, 2017, 10:46 AM
 * https://leetcode.com/problems/array-partition-i/discuss/
 */

#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

/*
 * 
 */

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        vector<int>::iterator it;
        sort(nums.begin(), nums.end());
        
        int result = 0;
        for (it = nums.begin(); it != nums.end() ; it+=2) {
//            cout << *it << " ";
            result += *it;
        }
        
        return result;

    }
};

int main() {
    int arr[] = {1,4,3,2};
    vector<int>::iterator it;
    vector<int> nums;
    
    for (int num: arr) {
        nums.push_back(num);
    }
    
    Solution s;
    cout << s.arrayPairSum(nums);
    
//    for (it = nums.begin(); it != nums.end(); ++it) {
//        cout << *it << " ";
//    }

    return 0;
}

