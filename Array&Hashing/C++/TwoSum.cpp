#include <map>
#include <iostream>
#include <vector>
using namespace std;

class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        map<int, int> hash_map;

        vector<int> ret;

        for( int i = 0; i < nums.size(); i++ )
        {
            int diff = target - nums[i];

            if( hash_map.count(diff) )
            {
                ret = {i, hash_map[diff]};
            }

            hash_map[nums[i]] = i;
        }

        return ret;
    }
};

int main()
{
    vector<int> nums = {2,7,11,15};
    int target = 18;
    
    Solution s;
    
    vector<int> ret = s.twoSum(nums, target);

    for(int i=0; i< ret.size(); i++)
    {
        cout << ret[i] << endl;
    }
}