#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        map<string, vector<string>> hash_map;

        for( string s : strs )
        {
            int count[26] = {0}; 

            for( char c : s)
            {
                int tmp = int(c) - int('a');

            }
        }
    }
};

