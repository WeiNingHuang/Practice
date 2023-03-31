#include<vector>
#include<iostream>
#include<map>
using namespace std;

class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target){
        vector<int> res;

        map<int,int> mp;

        for(int i=0; i<nums.size(); i++){
            int diff = target - nums[i];

            if(mp.find(nums[i])==mp.end()){
                mp[i] = 1;
            }
            else{
                res.push_back(i);
            }
        }

    }
};

int main(){

    vector<int> nums = {1,2,3,4,5};
    Solution s = Solution();
    vector<int> res = s.twoSum(nums, 8);

    for( int i : res){
        cout << i << endl;
    }

    return 0;
}