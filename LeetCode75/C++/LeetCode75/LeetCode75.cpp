#include <iostream>
#include <iterator>
#include "Array_String.cpp"


using namespace std;

int main()
{
    string word2 = "pqrs";
    string word1 = "zxcvasdf";

    Solution s;
    string ans = s.mergeAlternately_1768(word1, word2);

    for ( char c : ans )
    {
        cout << c;
    }
}
