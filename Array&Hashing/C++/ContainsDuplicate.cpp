#include <iostream>
#include <vector>
#include <map>
using std::vector;
using std::map;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> seen;

        for each(int val in nums)
        {
            if (!seen.count(val))
                seen[val] = 1;
            else
                return false;
        }

        return true;
    }
};

int main()
{   
    vector<int> nums = {1,2,3,1};
    Solution s;
    auto ans = s.containsDuplicate(nums);

    std::cout <<ans ;
}