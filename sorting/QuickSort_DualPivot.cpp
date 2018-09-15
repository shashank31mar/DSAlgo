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
		
	int pivot1 = arr[low];
	int pivot2 = arr[high];
	
	if (pivot1 > pivot2) {
		swap(arr,low, high);
		pivot1 = arr[low];
		pivot2 = arr[high];
	}
	
	else if (pivot1 == pivot2) {
		while (pivot1 == pivot2 && low < high) {
			pivot1 = arr[low];
			low++;
		}
	}
	
	int leftMark = low +1;
	int rightMark = high;
	int lt = low;
	
	while(leftMark <= rightMark) {				
		if(pivot1 > arr[leftMark])			//LEFT
			swap(arr, leftMark++, lt++);
			
		else if(pivot2 < arr[leftMark])	//RIGHT
			swap(arr, leftMark, rightMark--);
			
		else
			leftMark++;					//EQUAL
	}
	
	QuickSort(arr, low, lt-1);
	QuickSort(arr, lt+1, rightMark-1);
	QuickSort(arr, rightMark+1, high);
	
	
//	QuickSort(arr, low, lt-1);
//	QuickSort(arr, gt+1, high);
	
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
	
	QuickSort(uArr,0,uArr.size()-1);
	
	for(int i=0; i<uArr.size(); i++) {
		cout << uArr[i] << " ";
	}
	return 0;
}