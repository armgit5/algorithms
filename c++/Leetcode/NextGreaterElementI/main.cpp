/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: asuwansiri
 *
 * Created on October 9, 2017, 2:20 PM
 * https://leetcode.com/problems/next-greater-element-i/description/
 */

#include <cstdlib>
#include <vector>
#include <stack>
#include <map>
#include <iostream>

using namespace std;

/*
 * 
 */
class Solution {
    public:
        vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
            stack<int> s;
            map<int,int> m;
            vector<int> result;
            
            for (int num: nums) {
                while (!s.empty() && s.top() < num) {
                    m[s.top()] = num;
                    s.pop();
                }
                s.push(num);
            }
            
            for (int num: findNums) {
                if (m.count(num)) {
                    result.push_back(m[num]);
                } else {
                    result.push_back(-1);
                }
            }

            
            return result;
        }
};

int main() {
    int findNumsArr[] = {5, 4, 3, 2, 1, 6};
    int numsArr[] = {9, 8, 7, 3, 2, 1, 6};
    vector<int>::iterator it;
    vector<int> findNums, nums, result;
    
    for (int num : findNumsArr) {
        findNums.push_back(num);
    }
    
    for (int num : numsArr) {
        nums.push_back(num);
    }
    
    Solution s;
    result = s.nextGreaterElement(findNums, nums);
    
    for (it = result.begin(); it != result.end(); ++it) {
        cout << *it << " ";
    }

    
    return 0;
}

