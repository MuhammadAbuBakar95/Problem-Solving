#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

int commonPrefixOneString(string s) {
	int len = s.size();
	for(unsigned i = 0; i < s.size() - 1; i++) {
		unsigned first =  0;
		unsigned second = i + 1;
		while(second < s.size() && s[first] == s[second]) {
			first++;
			second++;
			len++;
		}
	}
	return len;
}

vector<int> commonPrefix(vector<string> strings) {
	vector<int> lens;
	for(unsigned i = 0; i < strings.size(); i++) {
		lens.push_back(commonPrefixOneString(strings[i]));
	}
	return lens;
}

int main() {
	vector<string> vec;
	vec.push_back("abcabcd");
	vec.push_back("defabdfedac");
	vector<int> lens = commonPrefix(vec);
	for(unsigned i = 0; i < vec.size(); i++)
		cout << lens[i] << "\n";
}