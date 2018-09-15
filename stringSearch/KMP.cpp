#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int *prefixFunction(string P)
{
	int N = P.size(), k = 0;

	int *pi = (int *) malloc(sizeof(int) * N);
	for(int i=0; i<N; i++)
		pi[i] = 0;

	for(int i=1; i<N; i++)
	{
		while ( k > 0 && P[k] != P[i] )
			k = pi[k-1];

		if ( P[k] == P[i] )
			k = k+1;

		pi[i] = k;
	}

	return pi;
}

void KMP(string T, string P)
{
	int M = P.size(), N = T.size();

	int *pi = prefixFunction(P);

	int q=0;
	for(int i=0; i<N; i++)
	{
		while ( q>0 && P[q] != T[i] )
			q = pi[q-1];

		if ( P[q] == T[i] )
			q = q + 1;

		if ( q == M )
		{
			cout << "Pattern found at index : " << i - M + 1 << endl;
			q = pi[q-1];
		}
	}
}


int main()
{
	string aText = "shashashankgupta";
	string aPattern = "shashank";
	string T = "aaaaaaaaaa", P = "aaaa";
	KMP(aText, aPattern);

	return 0;
}


