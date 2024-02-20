#ifndef ANAGRAM_H
#define ANAGRAM_H
#include<string>
using namespace std;
class Anagram
{
public:
	Anagram();
	Anagram(string s1, string s2);
	string getFirst();
	string getSecond();
	bool isAnagram();
	void stringSort(string& s);
private:
	string first ;
	string second;
	string f;
	string s;
};
#endif
