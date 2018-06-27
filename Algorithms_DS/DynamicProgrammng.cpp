Search for a key in a Sorted and Rotated array
	findPivot()
	binarySearch()	on the 2 Different sub-arrays



Longest Common Subsequence
	If x == y  return common( 1 + A[x+1], B[y+1] );
	else return max common( A[x+1], B[y] ) , common( A[x], B[y+1] )

		int findLongestSubSequence(char* X, int mLength, 
									char *Y, int yLength)
		{
			if( xLength == 0 || yLength == 0 ) return 0;
			if( X[xLength - 1] == Y[yLength -1])
				return 1 + findLongestSubSequence(X, xLength - 1, Y, yLength - 1);
			else
				return max( findLongestSubSequence(X, xLength - 1, Y, yLength), 
							findLongestSubSequence( X, xLength, Y, yLength - 1));
		}

		/** Using a 2 Dimensional Array int table[xLength+1][yLength+1] **/
		int findLongestSubSequence(char* X, int mLength, 
									char *Y, int yLength)
		{
			int table[mLength+1][yLength+1] = { 0 };

			for( int i = 0; i <= mLength ; ++i)
			{
				for( int j = 0 ; j= < yLength; ++j)
				{
					if( i == 0 || y == 0) table[i][j] = 0;
					else if( X[i-1] == Y[j-1] )
						table[i]j] = table[i-1][j-1] + 1;
					else
						table[i][j] = std::max( table[i-1][j], table[i][j-1]);
				}
			}
			int index = table[mLength][yLength]
			char arr[  index + 1 ];

			int i = mLength 
			int j = yLength ;

			while( i > 0 && j > 0)
			{
				if( X[i-1] == Y[j-1])
				{
					arr[index-1] = X[i-1];
					--i;
					--j;
					--index;
				}
				else if( table[i-1][j] > table[i][j-1] )
					--i;
				else
					--j;
			}

			cout << arr << endl;
			return table[mLength][yLength];
		}

Longest Increasing Subsequence
Edit Distance
Minimum Partition
Ways to Cover a Distance
Longest Path In Matrix
Subset Sum Problem
Optimal Strategy for a Game
0-1 Knapsack Problem
Boolean Parenthesization Problem
Shortest Common Supersequence
Matrix Chain Multiplication
Partition problem
Rod Cutting
Coin change problem
Word Break Problem
Maximal Product when Cutting Rope
Dice Throw Problem
Box Stacking
Egg Dropping Puzzle

Greedy Problem

	Minimum time to finish all jobs with given constraints
	Job Sequencing Problem | Set 2 (Using Disjoint Set)
	Minimum sum of two numbers formed from digits of an array
	Find Smallest number with given number of digits and digits sum
	Connect n ropes with minimum cost --  /*** DONE .... USE A MIN HEAP ***/
	Minimum number of Platforms required for a railway/bus station ----- sort both Arrival and Destination .... Put +1 for Arrival and -1 for destination
			Perform a cummulative sum ... largets number is the minimum platforms required.. 
	Minimum sum of absolute difference of pairs of two arrays
	Maximize sum of consecutive differences in a circular array
	Paper cut into minimum number of squares
	Minimize sum of product of two arrays with permutation allowed
	Lexicographically smallest array after at-most K consecutive swaps
	Rearrange characters in a string such that no two adjacent are same
	Maximum height pyramid from the given array of objects
	Minimum cost for acquiring all coins with k extra coins allowed with every coin
	Maximum sum possible equal to sum of three stacks
	Maximize array sum after k-negations | Set 1
	Maximize array sum after k-negations | Set 2
	Rearrange a string so that all same characters become d distance away
	Minimum Cost to cut a board into squares
	Minimize cash flow among friends
	Minimum edges to reverse to make path from a source to a destination
	Minimize the maximum difference between the heights of towers

Divide and Conquer

Standard Algorithms :

		Intoduction to Divide and Conquer
		Binary Search
		Merge Sort
		Quick Sort
		Calculate pow(x, n)
		Closest Pair of Points
		Strassen’s Matrix Multiplication
		Karatsuba algorithm for fast multiplication
		Count Inversions
		Multiply two polynomials
		Tiling Problem
		Convex Hull (Simple Divide and Conquer Algorithm)
		Quickhull Algorithm for Convex Hull
		Binary Search Based :

		Median of two sorted arrays
		Median of two sorted arrays of different sizes
		Check for Majority Element in a sorted array
		Count number of occurrences (or frequency) in a sorted array
		Find a Fixed Point
		Closest Pair of Points | O(nlogn) Implementation ( Find the distance from 0.0. using pythogarus theorem and sort them ..... )
		Find the maximum element in an array which is first increasing and then decreasing
		Find a peak element
		Find the number of zeroes
		Find the minimum element in a sorted and rotated array
		Find the point where a monotonically increasing function becomes positive first time
		Find the missing number in Arithmetic Progression
		Floor in a Sorted Array
		Find the element that appears once in a sorted array
		Find the only repeating element in a sorted array of size n
		K-th Element of Two Sorted Arrays
		Find index of an extra element present in one sorted array
		Find bitonic point in given bitonic sequence
		Find the Rotation Count in Rotated Sorted array
		>> More

		Misc :

		Largest Rectangular Area in a Histogram | Set 1
		Maximum and minimum of an array using minimum number of comparisons
		Write you own Power without using multiplication(*) and division(/) operators
		Program to count number of set bits in an (big) array
		Maximum Subarray Sum
		Search in a Row-wise and Column-wise Sorted 2D Array
		The Skyline Problem
		Square root of an integer
		Longest Common Prefix
		Find frequency of each element in a limited range array in less than O(n) time
			First Method using Map and Count 
			Second : Recursively divide the Array into subarrays. If start and End Element are same, then get the Count of the Sub_Array. 
		Find cubic root of a number
		Minimum difference between adjacent elements of array which contain elements from each row of a matrix
		Easy way to remember Strassen’s Matrix Equation
		Allocate minimum number of pages
		Place k elements such that minimum distance is maximized
		Search element in a sorted matrix
		Find a peak element in a 2D array
		Collect all coins in minimum number of steps
			If Found -- Bolts Exist for the Nuts
			Put all Coins inside different Stacking
			Start pulling from the bottom


		Shuffle 2n integers in format {a1, b1, a2, b2, a3, b3, ……, an, bn} without using extra space

BackTracking
	
Misc:

		Commonly Asked Algorithm Interview Questions | Set 1
		Given a matrix of ‘O’ and ‘X’, find the largest subsquare surrounded by ‘X’
		Nuts & Bolts Problem (Lock & Key problem)
			Traverse the Nuts Array and Create a HashMap
			Traverse the Bolts Array and Find it in the HashMmap
							#include <iostream>
							#include <unordered_map>
							using namespace std;

							void nutboltmatch(char nuts[], char bolts[], int n)
							{
								unordered_map<char,int> hash;
								
								
								for(int i = 0 ; i < n; ++i )
								{
									hash[nuts[i]] = i;
								}
								
								for(int i = 0 ; i < n; ++i )
								{
									if (hash.find(bolts[i]) != hash.end() )
										nuts[i] = bolts[i];
								}
								
								cout << "Nuts : ";
								for(int i = 0 ; i < n; ++i )
								{
									cout << nuts[i] << " : ";
								}
								
								cout << endl;
								cout << "Bolts : ";
								for(int i = 0 ; i < n; ++i )
								{
									cout << bolts[i] << " : " ;
								}

							}
							// Driver code
							int main()
							{
							    char nuts[] = {'@', '#', '$', '%', '^', '&'};
							    char bolts[] = {'$', '%', '&', '^', '@', '#'};
							    int n = sizeof(nuts) / sizeof(nuts[0]);
							    nutboltmatch(nuts, bolts, n);
							    return 0;
							}
		Flood fill Algorithm – how to implement fill() in paint?
		Given n appointments, find all conflicting appointments --- Using a Interval Tree .... Low values is used to Maintain the BST Nature.... 
		Check a given sentence for a given set of simple grammer rules
		Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array
		How to check if two given sets are disjoint?	
				Sort first set
					Perform Binary Search of every Element in the second set.

		Minimum Number of Platforms Required for a Railway/Bus Station
				Sort both the Arrival and Departure Array
				Start loop .... while( i = < && j < n )
									{
										if( arrival[i] < depature[i])
											// Increment Platorm
											++Platoform
											++i
										else
											decrement Platforms
											j++
									}
		Length of the largest subarray with contiguous elements | Set 1
		Largest Sum Contiguous Subarray

		int max_so_far = 0 ;
		int max_ending = INT_MIN;
		int start = end = 0;
		int i = 0;

		for( int i = 0 ; i < n ; ++i)
		{
			max_ending = max_ending + arr[i];
			if( max_ending <= 0)
			{
				max_ending = 0 ;
				s = i + 1;
			}

			if( max_so_far < max_ending)
			{
				max_so_far = max_ending;
				start = s ;
				end = i;
			}
		}

		return max_so_far ;

		for( int i = 0 ; i < n ; ++i )
		{
			int min = arr[i];
			int max = arr[i];

			for( int j = i + 1; j < n ; ++j)
			{
				min = min(min, arr[j]);
				max = max(max, arr[j]);

				if( max - min == j - i)
				{
					max_len = max( max_len, max - min + 1)
				}
			}
		}

		return max_len ;
		Length of the largest subarray with contiguous elements | Set 2
		Contiguos subsequence with no 2 consecutive
		Contiguos subsequence with no 3 consecutive
			int maxLength = 0 ;
			int start = 0 ;
			int min = arr[0];
			int max = arr[0];

			for( int i = 0 ; i < n ; ++i)
			{
				for( int j = i + 1; j < n ; ++j)
				{
					min = min(i, j);
					max = max(i, j);


					if( max - min == j - i + 1)
					{
						maxLen = j - i + 1;
						if maxLen > alreadyComputed
							alreadyComputed = maxLen;
					}
				}
			}

					}
				}
				

				if( )
			}
		Print all increasing sequences of length k from first n natural numbers
		Given two strings, find if first string is a subsequence of second
		Snake and Ladder Problem

				/** Snakes and Ladder **/
				struct Node
				{
					int vertex ; // Vertex Number ... Box in the Board
					int distance ; // Distance of the Box from Beginning
				}

				int getMinDice(int moves[], int numberOfBoxes)
				{
					bool *visited = new bool(N);
					for( int i = 0 ; i < N ; ++i )
						visited[i] = false; // Initially all are not visited
						
					// Create a Queue of Node
					Queue<Node> iQueue;
					
					// Push first Box inside the Queue
					Node n;
					n.vertex = 0 ;
					n.distance = 0;
					
					iQueue.push_back(n);
					visited[0] = true;
					Node a ;
					
					while( !iQueue.empty() )
					{
						a = iQueue.front();
						int vertex = a.vertex ;
						
						if( vertex == N )
							break;
							
						iQueue.pop();
							
						for( int j = vertex + 1 ; j < vetex + 6 && j < N ; ++j )
						{
							// If J vertex is not visited
							if( visited[j] != true )
							{
								Node intenal;
								internal.distance = j+1;
								visited[j] = true;
								
								if( move[j] != -1 ) // Has a Ladder or a Snake
								{
									intenal.vertex = move[j];
								}
								else
									intenal.vertex = j;
									
								
							}
							
							iQueue.push_back(internal);
						}
					}
					
					return a.distance;
				}


		Write a function that returns 2 for input 1 and returns 1 for 2
		Connect n ropes with minimum cost
			Using Min_heap --- priority_queue<int, vector<int>, greater<int> >
			Keep on Adding top 2 Minimum values and add them back to priority_queue
			Continue till priority_queue.size() > 1

		Find the number of valid parentheses expressions of given length
		Longest Monotonically Increasing Subsequence Size (N log N): Simple implementation
		Generate all binary permutations such that there are more 1’s than 0’s at every point in all permutations
		Lexicographically minimum string rotation
		Construct an array from its pair-sum array
		Program to evaluate simple expressions

		Longest Palindrome string 
			Manchester Algorithm

		void findLongestPalindrome(const string& str)
		{
				int start = low = high = maxLentgh = 0;
				for( int i = 1; i < str.length(); ++i)
				{
					// Find Largest Even Length Palindrome
					low = i - 1
					high = i ;
					while( low >=0 && high < str.length() && str[low] == str[high])
					{
						if( high - low + 1 > maxLentgh)
						{
							maxLentgh = high - low + 1;
							start = low;
						}
						--low;
						++high;
					}

					// Find Largest Odd Length Palindrome
					low = i - 1;
					high = i + 1;
					while( low >= 0 && high < str.length() && str[low] == str[high])
					{
						if( maxLentgh < high - low + 1)
						{
							maxLentgh = high - low + 1;
							start = low;
						}
						--low;
						++high;
					}
				}
		}
		Check if characters of a given string can be rearranged to form a palindrome
			1. Append Same string to the given string.
				example ... given string = AAABA
							new String = AAABAAAABA
			2.	Now Find all Palindromes of length that is equal to given input string ...
			3.	If found, then it can be rotated to form a palindrome .....

			void expand(int low, int high, set<string> mySet, string str)
			{
				while( low > 0 && high < str.length() && str[low] == str[high])
				{
					mySet.insert(str.substr(low, high - low + 1 ));
					++low;
					--high;
				}
			}
			
			void findAllPalindromes(string str)
			{
				int len = str.length();
				for( int i = 0 ; i < len ; ++i)
				{
					// Find all Odd Length Palindromes
					expand(i, i, mySet, str);

					// Find all Even Length Palindromes
					expand(i, i+1, mySet, str);
				}
			}

			A set of characters can form a palindrome if at most one character occurs odd number of times and all characters occur even number of times.

			/** Print Longest Palindromic word in a Sentence **/
			string longestPalindrom(const string& incomingSentence)
			{

			}
			bool isPalindrome(const string& iWord)
			{
				// Function to check whether a word is a palindrome or not ...
				int low = 0;
				int high = iWord.length() - 1;

				while( low <= high)
				{
					if( str[low] == str[high] )
					{
						low++;
						high--;
					}
					else
						return false;
				}

				return true;
			}


		Print all pairs of anagrams in a given array of strings
			Sort the Array of Strings and run a linear compare .....