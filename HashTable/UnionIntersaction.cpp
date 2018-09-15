#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int getHashKey(unordered_map<int, int>& hash, int data) {
	unordered_map<int, int>::hasher fn = hash.hash_function();
	
	int key =  fn(data);
//	cout << "data is : " << data << " hash key is : " << key << endl;
	return key;
}

vector<int> Union(vector<int> arr1, vector<int> arr2) {
	vector<int> result;
	unordered_map<int, int> hash;
	
	for(auto item: arr1) {
		pair<int, int> data(getHashKey(hash,item), item);
		hash.insert(data);
		
		result.push_back(item);
	}
  
	for(auto item: arr2) {
		if(hash.find(getHashKey(hash,item)) == hash.end())
		{
			pair<int, int> data(getHashKey(hash, item), item);
			hash.insert(data);
			result.push_back(item);
		}
	}
	
	return result;
}

vector<int> Intersection(vector<int>arr1, vector<int> arr2) {
	vector<int> result;
	unordered_map<int, int> hash;
	
	for(auto item: arr1) {
		pair<int, int> data(getHashKey(hash,item), item);
		hash.insert(data);
	}
	
	for(auto item: arr2) {
		if(hash.find(getHashKey(hash,item)) != hash.end()) {
			pair<int, int> data(getHashKey(hash, item), item);
			hash.insert(data);
			result.push_back(item);
		}
	}
	
	return result;
}

int main() {

	vector<int> arr;
	vector<int> arr1;
	
	arr.push_back(2);
	arr.push_back(4);
	arr.push_back(6);
	arr.push_back(1);
	arr.push_back(2);
	
	arr1.push_back(2);
	arr1.push_back(7);
	arr1.push_back(3);
	arr1.push_back(5);
	
	cout << "Union is : " << endl;
	for(auto item: Union(arr, arr1)) {
		cout << item << " ";
	}
	cout << endl;
	
	cout << "Intersaction is : " << endl;
	for(auto item: Intersection(arr, arr1)) {
		cout << item << " ";
	}
	cout << endl;
	return 0;
}