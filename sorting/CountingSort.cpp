#include <iostream>
#include <vector>
#include <string.h>

#define RANGE 255

using namespace std;

void countSort(char* str) {
	vector<int> count;
	count.reserve(RANGE);
	
	char output[strlen(str)];
	
	for(int i =0; i < strlen(str); i++) {
		++count[int(str[i])];
	}
	
	for(int i=1; i < RANGE ; i++) {
		count[i] = count[i-1] + count[i];
	}
	
	for(int i=0; i< strlen(str); i++) {
		output[count[int(str[i])] - 1] = str[i];
		--count[int(str[i])];
	}
	
	for(int i = 0 ; i < strlen(str); i++) {
		str[i] = output[i];
	}
}

int main() {
	
	char arr[] = "shashank gupta";
	
	countSort(arr);
	
	string sortedString(arr);
	
	cout << "sorted string is : " << sortedString << endl;

	return 0;
}