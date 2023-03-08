#include <map>
#include <vector>
#include <iostream>

using std::vector;
using std::map;
using std::string;

class Solution {
public:
    bool isAnagram(string& s, string& t) 
    {
        map<char, int> seen;

        if( s.size() != t.size())
            return false;

        for(int i = 0; i < s.size(); i++)
        {
            if( !seen.count(s[i]) )
            {
                seen[s[i]] = 1;
            }
            else
            {
                seen[s[i]] ++;
            }
        }

        for( int j = 0; j < t.size(); j++)
        {
            if( !seen.count( t[j]) )
            {
                return false;
            }
            else
            {
                seen[ t[j] ] -- ;
            }
        }

        for(int k = 0 ; k < seen.size(); k++)
        {
            if( seen[k] != 0 )
            {
                return false;
            }
        }
   
        return true;
    }
};

int main()
{
    string s = "anagram";
    string t = "nagaram";

    Solution sol;

    std::cout << sol.isAnagram(s, t);
}