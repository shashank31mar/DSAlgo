#include <iostream>
#include <vector>
using namespace std;

void Copy(vector<int>& buf, int low, int high, vector<int>& arr) {
	for(int i = low; i < high; i++) {
		buf[i] = arr[i];
	}
}

void Merge(vector<int>& arr, int low, int mid, int high) {
	int i = low;
	int j = mid +1;
	int k = low;
	
	vector<int> buf;
	buf.reserve(21);
	
	while (i <= mid && j <= high) {
		
		if(arr[i] > arr[j]) {
			buf.push_back(arr[j]);
			j++;
			k++;
		}
		else {
			buf.push_back(arr[i]);
			i++;
			k++;
		}
	}
	
	while(j <= high) {
		buf.push_back(arr[j]);
		j++;
		k++;
	}
	
	while(i <= mid) {
		buf.push_back(arr[i]);
		k++;
		i++;
	}
	
	for(int x = low; x < k; x++) {
		arr[x] = buf[x];
	}

}

void MergeSort(vector<int>& arr, int low, int high, vector<int>& buf) {
	if(high -low < 2)
		return ;
		
	int mid = high/2 + low/2;
	
	MergeSort(arr, low, mid, buf);
	MergeSort(arr, mid+1, high, buf);
	
	Merge(arr, low, mid, high);
}

int main() {
	vector<int> uArr;
	vector<int> buf;
	uArr.reserve(21);
	buf.reserve(21);
	
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
	
	MergeSort(uArr,0,uArr.size()-1, buf);
	
	for(int i=0; i<uArr.size(); i++) {
		cout << uArr[i] << " ";
	}
	return 0;
}