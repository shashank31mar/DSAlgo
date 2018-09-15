#include <iostream>
#include <vector>
using namespace std;

void initialize(vector<int>& aTable) {
	aTable[0] = -1;
	aTable[1] = 0;
}

void KMPTable(string& iPattern, vector<int>& iTable) {
	//iTable.reserve(iPattern.length());
	cout << "inside table" << endl;
	int pos = 1;	//current position in table
	int cnd = 0;	//Index in W
	
	initialize(iTable);
	
	//Example abababca
	//shashank
	while(pos < iPattern.length()) {
		if(iTable[pos] == iTable[cnd]) {
			++cnd;
			iTable[pos] = cnd;
	//		cout << iTable[pos] << endl;
			 ++pos;
		}
		else if(cnd > 0) {
			cnd = iTable[cnd-1];
		}
		else {
			iTable[pos] = 0;
			++pos;
		}
	}
	//cout << "after while"  << iTable[3] << endl;
	
	for(int i=0; i < iTable.size(); i++) {
		cout << iTable[i] << " ";
	}
}

void KMPSearch(string& iText, string& iPattern) {
	
	int m = 0;			//Position in Text
	int i = 0;			//Position in Pattern
	
	vector<int> aPreComputationTable;
	aPreComputationTable.reserve(iPattern.length());
	
	KMPTable(iPattern, aPreComputationTable);
	//cout<< iPattern[2] << endl;
	//cout << iPattern.length() << endl;
	while (m < iText.length()) {
		if(iPattern[i] == iText[m]) {
			++i;
			++m;
		}
		
		if(i == iPattern.length()) {
				cout<< "index found at : " << m << endl;
				i = aPreComputationTable[i-1];
		}
			
		else if(m < iText.length() && iPattern[i] != iText[m]) {
			if(i > -1) {
				//m = m + i - aPreComputationTable[i];
				i = aPreComputationTable[i-1];
			}
			else {
				++i;
				//++m;
			}
		}
		
	}
	//return iText.length();
}

int main() {

	string aText = "shashashankgupta";
	string aPattern = "shashank";
	
	KMPSearch(aText, aPattern);
	
	
	return 0;
}
