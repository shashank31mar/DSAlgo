#include <iostream>
#include <vector>
using namespace std;

void swap(vector<int>& arr, int low, int high) {
	int temp = arr[low]	;
	arr[low] = arr[high];
	arr[high] = temp;
}

void QuickSort(vector<int>& arr, int low, int high) {
	
	if (high <= low)
		return;
		
	int lt = low;
	int rightMark = high;
	int leftMark = low + 1;
	int pivotIndex = low;
	int pivotValue = arr[pivotIndex];
	
	while(leftMark <= rightMark) {				
		if(pivotValue > arr[leftMark])			//LEFT
			swap(arr, leftMark++, lt++);
			
		else if(pivotValue < arr[leftMark])	//RIGHT
			swap(arr, leftMark, rightMark--);
		else
			leftMark++;						//EQUAL
	}
	
	QuickSort(arr, low, lt-1);
	QuickSort(arr, rightMark+1, high);
}

int main() {
	
	vector<int> uArr;

	for (int i =  10; i > 0; i--) {
		uArr.push_back(i);
	}
	/*
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
	*/
	QuickSort(uArr,0,uArr.size()-1);
	
	for(int i=0; i<uArr.size(); i++) {
		cout << uArr[i] << " ";
	}
	return 0;
}