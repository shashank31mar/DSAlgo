#include <iostream>
#include <vector>
using namespace std;

bool compare(vector<int>& arr1, vector<int>& arr2) {
	
	for(int i=0; i< 256; i++) {
		if(arr1[i] != arr2[i])
			return false;
	}
	return true;
}

void Anagram(string& text,string& pattern) {
	vector<int> textCount;
	vector<int>patternCount;
	
	textCount.reserve(256);
	patternCount.reserve(256);
	
	for(int i=0; i < pattern.length() ; i++) {
		textCount[int(text[i])] = textCount[int(text[i])] + 1;
		patternCount[int(pattern[i])]++;
	}
	
	for(int i = pattern.length();  i < text.length(); i++) {
		if( compare(textCount, patternCount)) {
			cout << "index found at : " << i-pattern.length() << endl;
		}
		
		textCount[int(text[i])]++;
		textCount[int(text[i-pattern.length()])]--;

	}
}

int main() {

	string text = "shashashankgupta";
	string pattern = "shas";
	
	Anagram(text, pattern);
	return 0;
}
