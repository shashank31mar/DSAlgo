#include <iostream>
#include <vector>
using namespace std;

bool findEmptyPosition(vector<vector<int> >& arr, int& row, int& col) {
	for(row=0;row<9;++row) {
		for(col=0;col<9;++col) {
			if(arr[row][col] == 0)
				return true;
		}
	}
	return false;
}

bool usedInRow(vector<vector<int> >& arr, int row, int value) {
	for(int i=0; i < 9; i++) {
		if(arr[row][i] == value) {
			return true;
		}
	}
	return false;
}

bool usedInCol(vector<vector<int> >& arr, int col, int value) {
	for(int i=0; i < 9; i++) {
		if(arr[i][col] == value) {
			return true;
		}
	}
	return false;	
}

bool usedInBox(vector<vector<int> >& arr, int row, int col, int value) {
	for(int i=0; i < 3; ++i) {
		for(int j=0; j<3;++j) {
			if(arr[i+row][j+col] == value) {
				return true;
			}
		}
	}
	return false;
}

bool isSafePosition(vector<vector<int> >& arr, int row, int col, int value) {
	
	return !usedInRow(arr,row, value) &&
			!usedInCol(arr,col,value) &&
			!usedInBox(arr, row - row%3,col - col%3,value);
}

void printGrid(vector<vector<int> >& arr)
{
    for (int row = 0; row < 9; row++)
    {
		for (int col = 0; col < 9; col++)
			cout << arr[row][col] << " ";
		cout << endl;
    }
}

bool solveSudoku(vector<vector<int> >& arr) {
	
	int row, col;
	
	if(!findEmptyPosition(arr,row,col)) {
		return true;
	}
	
	for(int i=1; i<= 9; ++i) {
		if(isSafePosition(arr,row,col,i)) {
			arr[row][col] = i;
			
			if(solveSudoku(arr))
				return true;
				
			arr[row][col] = 0;
		}	
	}
	return false;
}

int main() {
	
	vector<vector<int> > arr;
/*	arr.resize(9);
	arr[0].resize(9);
	arr[1].resize(9);
	arr[2].resize(9);
	arr[3].resize(9);
	arr[4].resize(9);
	arr[5].resize(9);
	arr[6].resize(9);
	arr[7].resize(9);
	arr[8].resize(9);
*/	
arr = {
	{3, 0, 6, 5, 0, 8, 4, 0, 0},
	{5, 2, 0, 0, 0, 0, 0, 0, 0},
	{0, 8, 7, 0, 0, 0, 0, 3, 1},
	{0, 0, 3, 0, 1, 0, 0, 8, 0},
	{9, 0, 0, 8, 6, 3, 0, 0, 5},
	{0, 5, 0, 0, 9, 0, 6, 0, 0},
	{1, 3, 0, 0, 0, 0, 2, 5, 0},
	{0, 0, 0, 0, 0, 0, 0, 7, 4},
	{0, 0, 5, 2, 0, 6, 3, 0, 0}
	};
	
	if(solveSudoku(arr)) {
		printGrid(arr);	
	}
	return 0;
}