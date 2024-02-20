#include<iostream>
#include "Anagram.h"
#include<string>
using namespace std;

Anagram::Anagram()
{
	first.clear();
	second.clear();
}

Anagram::Anagram(string s1,string s2)
{
	first = s1;
	second = s2;
	f = s1;
	s = s2;
}

string Anagram::getFirst()
{
	return f;
}

string Anagram::getSecond()
{
	return s;
}

void Anagram::stringSort(string& s)
{
	for (int i = 0; i<int(s.length() - 1); i++)
	{
		char currentMin = s[i];
		int currentMinIndex = i;

		for (int j = i+ 1; j<int(s.length()); j++)
		{
			if (currentMin > s[j])
			{
				currentMin = s[j];
				currentMinIndex = j;
			}
		}
		if (currentMinIndex != i)
		{
			s[currentMinIndex] = s[i];
			s[i] = currentMin;
		}
	}
}

bool Anagram::isAnagram()
{
	stringSort(first);
	stringSort(second);
	if (first != second || first.empty())
		return false;
	return true;
}