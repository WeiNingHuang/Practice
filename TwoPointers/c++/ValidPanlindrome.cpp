#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) 
    {
        string new_s;

        int l = 0;
        int r = s.size() - 1;

        while( l <= r )
        {
            if( s[l] == s[r])
            {
                l ++;
                r --;
            }
            
        }
    }
};

int main()
{
    vector<int> v = {1,2,3,4,5};

    for(int i : v )
    {
        cout << i << endl;
    }
}