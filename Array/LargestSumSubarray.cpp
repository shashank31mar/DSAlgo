#include <iostream>
#include <vector>
using namespace std;

//does not work if all are negative
//This problem can be done using divide and conquer
int LSCSA(vector<int> arr) {
	int max_so_far = 0;
	int max_ending_here = 0;
	
	for(auto item: arr) {
		max_ending_here =  max_ending_here + item;
		
		if(max_ending_here < 0) {
			max_ending_here = 0;
		}
		
		if(max_so_far < max_ending_here) {
			max_so_far = max_ending_here;
		}
	}
	
	return max_so_far;
}

int main() {

	vector<int> arr;
	arr.push_back(2);
	arr.push_back(-20);
	arr.push_back(6);
	arr.push_back(-4);
	arr.push_back(-3);
	arr.push_back(7);
	arr.push_back(1);
	arr.push_back(2);
	arr.push_back(-5);
	arr.push_back(1);
	arr.push_back(-2);
	
	cout << "largest sum is " << LSCSA(arr) << endl;
	return 0;
}