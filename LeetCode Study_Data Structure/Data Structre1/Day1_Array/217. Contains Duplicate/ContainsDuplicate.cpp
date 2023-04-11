// Given an integer array nums,
// return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: true
// Example 2:
// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true


#include<vector>
#include<iostream>
#include<map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> mp;

        // for(int i=0; i<nums.size();i++){
        //     cout<< nums[i] << endl;
        // }

        // new way iterate for vector
        for( int i: nums)
        {
            if(mp.find(i) == mp.end()){
                mp[i] = 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};

int main(){
    vector<int> test = vector{1,2,3,2};
    Solution s = Solution();

    bool res = s.containsDuplicate(test);

    cout << res;
    return 0;
}
