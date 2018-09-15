#include <iostream>
using namespace std;

//Denominations available are --> 1, 5, 10, 20
int makeChange(int sum, int denom) {
	int next_denom = 0;
	
	switch(denom) {
		case 20:
			next_denom = 10;
			break;
		case 10:
			next_denom = 5;
			break;
		case 5:
			next_denom = 1;
			break;
		case 1:
			return 1;
	}
	
	int ways = 0;
	for(int i = 0; i*denom <= sum ; i++) {
		//cout << "before denom : " << denom << endl;
		ways += makeChange(sum - i*denom, next_denom);
		//cout << "denom : " << denom << endl;
		cout << "next_denom : " << next_denom << endl;
	}
	return ways;
}

int main() {
	
	cout << makeChange(5,20) << endl;
	return 0;
}