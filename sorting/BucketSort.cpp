#include <iostream>
#include <vector>

using namespace std;

int Hash(int value) {
	return value/10;	
}

void sort(vector<int>& arr) {
	int key, j, temp;
	for(int i=1; i <arr.size(); i++) {
		key  = arr[i];
		j = i-1;
		while(j>=0 && key < arr[j]) {
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = key;
	}
}

void bucketSort(vector<int>& aUArr) {
	
	vector<int> arr[aUArr.size()];
	
	for(int i=0; i < aUArr.size(); i++) {
		int hashvalue = Hash(aUArr[i]);
		
		if(hashvalue > aUArr.size()) {
			hashvalue = aUArr.size() - 1;
		}
		
		arr[hashvalue].push_back(aUArr[i]);
	}
	
	for(int i=0; i < aUArr.size() ; i++) {
		sort(arr[i]);
	}
	
	for(int i=0; i < aUArr.size(); i++) {
		for (int j=0; j<arr[i].size(); j++) {
			cout << arr[i][j] << " ";
		}
	}
}

int main() {
	vector<int> uArr;

	uArr.push_back(25);
	uArr.push_back(44);
	uArr.push_back(13);
	uArr.push_back(34);
	uArr.push_back(27);
	uArr.push_back(11);
	uArr.push_back(4);
	uArr.push_back(9);
	uArr.push_back(45);
	uArr.push_back(33);
	uArr.push_back(27);
	uArr.push_back(28);
	uArr.push_back(42);
	uArr.push_back(6);
	uArr.push_back(49);
	uArr.push_back(31);
	uArr.push_back(37);
	uArr.push_back(23);
	uArr.push_back(14);
	uArr.push_back(28);
	uArr.push_back(41);
	
	bucketSort(uArr);
	return 0;
}