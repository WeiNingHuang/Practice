#include <iostream>
#include <string>
#include "Array_String.h"

using namespace std;

string Solution::mergeAlternately_1768(string word1, string word2)
{
	string ans;
	string::iterator it1 = word1.begin();
	string::iterator it2 = word2.begin();

	while ( true )
	{
		if ( it1 != word1.end() && it2 != word2.end() )
		{
			ans.push_back( *it1 );
			ans.push_back( *it2 );
			it1++;
			it2++;
		}
		else if ( it1 == word1.end() && it2 != word2.end() )
		{
			ans.push_back( *it2 );
			it2++;
		}
		else if ( it1 != word1.end() && it2 == word2.end() )
		{
			ans.push_back( *it1 );
			it1++;
		}
		else
		{
			break;
		}
	}
	return ans;
}