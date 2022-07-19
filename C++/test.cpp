#include <iostream>
#include <vector>
#include <map>
using std::vector;
using std::map;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> seen;

        bool isDuplicate = false;

        for(int i =0; i< nums.size(); i ++)
        {
            int val = nums[i];
            
            if( !seen.count(val) )
                seen[nums[i]] = val;
            else
                isDuplicate = true;       
        }
        return isDuplicate;
    }
};

int main()
{   
    vector<int> nums = {1,2,3,1};
    Solution s;
    auto ans = s.containsDuplicate(nums);

    std::cout <<ans ;
}