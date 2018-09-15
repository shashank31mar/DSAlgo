#include <iostream>
using namespace std;

int GetMinCount(int total, int* coins, int length)
{
    int* counts = new int[total + 1];
    counts[0] = 0;
   
    const int MAX = 0x7FFFFFFF;

    for(int i = 1; i <= total; ++ i)
    {
        int count = MAX;
        for(int j = 0; j < length; ++ j)
        {
        	//cout<< "coins : " << counts[i - coins[j]] << endl;
            if(i - coins[j] >= 0 && count > counts[i - coins[j]]) {
            	count = counts[i - coins[j]];
            	//cout << "coin is : " << coins[j] << endl;
            }
                
                
        }

        if(count < MAX)
            counts[i] = count + 1;
        else
            counts[i] = MAX;
    }

    int minCount = counts[total];
    delete[] counts;

    return minCount;
}

int main() {

	int coins[] = {20,10,5,1};
	cout << "Minimum notes required are : " << GetMinCount(26,coins,4) << endl;
	
	return 0;
}











//Explanation
//https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/