#include <iostream>
#include <vector>
#include <stdlib.h>
#include <time.h>

using namespace std;

class RandomizedQuickSort {

	public:
		RandomizedQuickSort() {
			srand (time(NULL));
		}

		void QuickSort(vector<int>& aList) {
			_size = aList.size();
			QuickSortUtil(aList, 0, _size - 1);
		}

	private:
		void QuickSortUtil(std::vector<int>& aList, int start, int end) {

			if (start >= end) {
				return;
			}

			int aSplitPoint = partition(aList, start, end);

			QuickSortUtil(aList,start,aSplitPoint);
			QuickSortUtil(aList,aSplitPoint+1,end);
		}

		int getRandomIndex() {
			return rand() % _size;
		}

		int partition(std::vector<int>& aList, int start, int end) {
			int rand = getRandomIndex();
			cout << "Random is : " << rand << endl;
			int aPivot = aList[rand];

			int leftMark = start;
			int rightMark = end;
			bool done = false;
			int temp;
			while (!done) {
				while ((leftMark <= rightMark) && aList[leftMark] <= aList[aPivot]) {
					leftMark++;
				}

				while ((leftMark <= rightMark) && aList[rightMark] >= aList[aPivot]) {
					rightMark--;
				}

				if (rightMark < leftMark) {
					done = true;
				}
				else {
					temp = aList[leftMark];
					aList[leftMark] = aList[rightMark];
					aList[rightMark] = temp;
				}
			}
			temp = aList[rightMark];
			aList[rightMark] = aList[aPivot];
			aList[aPivot] = temp;

			/*for (int i=0; i < _size; i++) {
				cout << aList[i] << endl;
			}*/

			return rightMark;
		}

		int _size;
};

int main() {

	RandomizedQuickSort aRQS;

	std::vector<int> v;

	for (int i = 10; i>0; i--) {
		v.push_back(i);
		//cout << v[10-i] << endl;
	}

	aRQS.QuickSort(v);

	for (int i=0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout <<endl;

	return 0;
}