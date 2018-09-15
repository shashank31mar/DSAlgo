#include <iostream>
#include <vector>
#include <array>
using namespace std;

//Rolling Hash function 
//hash(txt[s+1, s+m]) = d(hash(txt[s, s+m-1] -txt[s]*h) + txt[s+m]) mod q;
//q = prime number
//h = d^m-1
//d = # of different characters in a string
//m = pattern length

int getHashValue(string t, int d, int h, int q, int m, int curIndex, int txtHash) {
	return (d*(txtHash - t[curIndex]*h) + t[curIndex+m])%q;
}

int calStringHash(string s, int len, int q) {
	int x=0;
	int d=256;
	for(int i=0; i < len ; ++i) {
		x = (d*x + s[i])%q;
	}
	
	return x;
}

void search(string& txt, string& pat) {
	int d = 256;
	int h = 1;
	int q = 31;
	int N = txt.length();
	int M = pat.length();
	int i = 0;
	int j = 0;
	
	int p = calStringHash(pat, M, q);
	int t = calStringHash(txt, M, q);
	
	for(i=0; i< pat.length()-1; i++) {
		h = (h*d)%q;
	}

	for(j=0; j <= N-M ; ++j ) {
		
		if(p==t) {
			for(i =0; i < M ; i++) {
				if(txt[i+j] != pat[i])
					break;
			}
			
			if(i==M)
				cout << "found at starting index : " << j << endl;
		}
		
		if(j<N-M) {
			t = getHashValue(txt,d,h,q,M,j,t);
			
			if(t<0) {
				t = t + q;
			}
		}
	}
}

int main() {
	
	string txt = "aaaaaaaaaaaaaaaa";
	string pat = "aaaaaaaaaaa";
	
	search(txt, pat);
	return 0;
}
