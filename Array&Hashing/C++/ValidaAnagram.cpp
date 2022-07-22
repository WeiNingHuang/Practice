#include <map>
#include <vector>
#include <iostream>

using std::vector;
using std::map;

class Solution {
public:
    bool isAnagram(string& s, string& t) {
        map<string, int> seen;

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