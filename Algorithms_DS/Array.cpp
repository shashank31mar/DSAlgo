Print odd and Even
Stock Span Algorithm
For each without temporary i

Erlang - The programming language used to script the real-time chat app system
FreeBSD - Advanced computer operating system handpicked for everything from desktops to tiny devices.
Yaws - An Erlang based web server that can also run as a standalone web server
Lighttpd - Another web server that is highly secure, swift, flexible and compliant with web server standards.
PHP - Open-source general-purpose scripting language best fit for web development.
XMPP - XMPP is the backbone that makes it possible to send real-time messages, online presence indicators, XML routing features and much more.
Array Questions:		

Search, insert and delete in an unsorted array
Search, insert and delete in a sorted array
Given an array A[] and a number x, check for pair in A[] with sum as x
	Using Map, store all Elements inside the Map with its second value as The Diff between number and sum
	Check if the number exists, Pair is Found....
	Sort the Array
		Start from left and right
Majority elements 		************** DONE ******************
Find the Number Occurring Odd Number of times 		/***************** USING XOR ***********/
Largest Sum Contiguous subarrays 					/***************** Kadenes Algorithm *******/
*****************************************************************************************************************
			max_current = max_global = A[0];

			for x in A[1:]
				max_current = max (x, max_current + x)

				if( max_current > max_global )
						update max_global to max_current

******************************************************************************************************************			
Find the Missing Number
Search an element in a sorted and pivoted Array 	/***************** Find the PIVOT and then search using Binary Search *************/
Merge an array of size n into another array of size m+n
Median of two sorted arrays
Write a program to reverse an array
Program for array rotation
Reversal algorithm for array rotation
Block swap algorithm for array rotation
Maximum sum such that no two elements are adjacent
Leaders in an Arrays 								/*************** DONE Start from Right .... If we find a number greater ... Print it... and change the leader ... ****/
Sort elements by frequency | Set 1
Count Inversions in an array
Two elements whose sum is closest to zero
Find the smallest and second smallest element in an array
Check for Majority Element in a sorted array
Maximum and minimum of an array using minimum number of comparisons
Segregate 0s and 1s in an Array 			/************************ Dutch National Flag **** Segregation of Numbers ****************************/
k largest(or smallest) elements in an array | added Min Heap method
Maximum difference between two Elements     //************************* DONE ******************************/
Union and Intersection of two sorted Arrays /************************* DONE ******************************/
Floor and Ceiling in a sorted array
A Product Array Puzzle
Segregate Even and Odd numbers /********************** Using 2 Indexes.... left and right.... increment and decrement .... swap if left < right ******** DONE **************/
Find the two repeating elements in a given arrays 			/******************* DONE ********************************
Sort an array of 0s, 1s and 2s		/******************************** Same Solution as Royal Dutch Flag Problem 	************************************************/
Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted
Find duplicates in O(n) time and O(1) extra space		/***************************** This can be done using a temp count[] and incrementing it as cout[arr[i]]++ *********/
Equilibrium index of an Arrays 						/********************************************** DONE ******************************************/
Linked List vs Array
Which sorting algorithm makes minimum number of memory writes ? /*********************** SELECTION/CYCLE Sort ****************************************/
Turn an image by 90 degree
Next Greater elements ******* DONE ***********
Check if array elements are consecutive | Added Method 3	*********** DONE ************
Find the smallest missing number
Count the number of occurrences in a sorted arrays ********************** Using Binary Search Find First and last occurrences of the Element , Calculate the Diff ****************
Interpolation search vs Binary search
Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
Maximum of all subarrays of size k (Added a O(n) method) 
Find whether an array is subset of another array | Added Method 3
Find the minimum distance between two numbers
Find the repeating and the missing | Added 3 new methods
Median in a stream of integers (running integers)
Find a Fixed Point in a given array
Maximum Length Bitonic Subarray
Find the maximum element in an array which is first increasing and then decreasing
Count smaller elements on right side
Minimum number of jumps to reach end
Implement two stacks in an array

Find subarray with given sum   ***********************************88 DONE *********************************************
for( int i = 0 ; i < n ; ++i)
{
	while( current_sum < sum && i < n )
	{
		++i;
		current_sum = current_sum - arr[i];
	}
	
	if( current_sum == givenSum )
		break;
		
	if( i < n )
		current_sum = current_sum + arr[i];
}

Dynamic Programming | Set 14 (Maximum Sum Increasing Subsequence)
Longest Monotonically Increasing Subsequence Size (N log N)
Dynamic Programming | Set 15 (Longest Bitonic Subsequence)
Find a sorted subsequence of size 3 in linear time
Construction of Longest Monotonically Increasing Subsequence (N log N)
Find the Increasing subsequence of length three with maximum product
Count all sub-sequence of a string in an string ...

void findAllSubSequence(string input, string pattern, string output)
{
	if( input.length() == 0 )
	{
		pattern == output )
		++count;
		return;
	}
	
	findAllSubSequence(input.substr(input[1], output )
	findAllSubSequence(input.substr[1], output + input[0] );
}


Find a triplet that sum to a given value
Find the smallest positive number missing from an unsorted array  **************************** SORT IT AND FIND IT ***********************
Find the two numbers with odd occurrences in an unsorted array
The Celebrity Problem

Largest subarray with equal number of 0s and 1s
Dynamic Programming | Set 18 (Partition problem)
Maximum Product Subarray
Find a pair with the given difference
Replace every element with the next greatest
Dynamic Programming | Set 20 (Maximum Length Chain of Pairs)
Find four elements that sum to a given value | Set 1 (n^3 solution)
Find four elements that sum to a given value | Set 2 ( O(n^2Logn) Solution)
Sort a nearly sorted (or K sorted) array
Maximum circular subarray sum
Find the row with maximum number of 1s
Median of two sorted arrays of different sizes
Shuffle a given array
Count the number of possible triangles
Iterative Quick Sort
Find the number of islands
Find the first circular tour that visits all petrol pumps
Arrange given numbers to form the biggest number
Pancake sorting
A Pancake Sorting Problem
Tug of War
Divide and Conquer | Set 3 (Maximum Subarray Sum)
Counting Sort
Merge Overlapping Intervals
Find the maximum repeating number in O(n) time and O(1) extra space
Stock Buy Sell to Maximize Profit
Rearrange positive and negative numbers in O(n) time and O(1) extra space
Sort elements by frequency | Set 2
Find a peak element
Print all possible combinations of r elements in a given array of size n
Given an array of of size n and a number k, find all elements that appear more than n/k times
Find the point where a monotonically increasing function becomes positive first time
Find the minimum element in a sorted and rotated array
Stable Marriage Problem
Merge k sorted arrays | Set 1
Radix Sort
Move all zeroes to end of array
Find number of pairs such that x^y > y^x
Count all distinct pairs with difference equal to k
Find if there is a subarray with 0 sum
Smallest subarray with sum greater than a given value
Sort an array according to the order defined by another array
Maximum Sum Path in Two Arrays
Sort an array in wave from                     ********************** DONE ************************************
K’th Smallest/Largest Element in Unsorted array                                     ************************* PRIORITY QUEUE *************************
K’th Smallest/Largest Element in Unsorted Array in Expected Linear times            ************************* PRIORITY QUEUE *************************
K’th Smallest/Largest Element in Unsorted Array in Worst Case Linear Time           ************************* PRIORITY QUEUE *************************
Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array
Find the closest pair from two sorted arrays ************** DONE *********
Given a sorted array and a number x, find the pair in array whose sum is closest to x ************* DONE *******************8
Count 1’s in a sorted binary array
Print All Distinct Elements of a given integer array
Construct an array from its pair-sum array
Subarray with no pair sum divisible by K
Find common elements in three sorted arrays                   ******************* DONE *************************
Find the first repeating element in an array of integers
Find the smallest positive integer value that cannot be represented as sum of any subset of a given array ******************** DONE
 *********************
 
 int findValue(int arr[], int size)
{
	int res = 1;
	
	for( int i = 0 ; i < size && arr[i] <= res ; ++i )
		res = res + arr[i];
		
	return res ;
}
Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’
Find position of an element in a sorted array of infinite Numbers 			************************** DONE ***********************
Can QuickSort be implemented in O(nLogn) worst case time complexity?
Check if a given array contains duplicate elements within k distance from each other ********************* NEED TO CHECK THIS WITH C++ Hashing ***************
Find the maximum and minimum values obtained by summing four of five integers. ******************* DONE *********************
Find the element that appears once
Replace every array element by multiplication of previous and next
Check if any two intervals overlap among a given set of intervals
Delete an element from array (Using two traversals and one traversal)
Find the largest pair sum in an unsorted Arrays *********************** DONE USING ONE PASS **************
Online algorithm for checking palindrome in a stream
Pythagorean Triplet in an array
Maximum profit by buying and selling a share at most twice
Find Union and Intersection of two unsorted Arrays
Count frequencies of all elements in array in O(1) extra space and O(n) time
Generate all possible sorted arrays from alternate elements of two given sorted arrays
Minimum number of swaps required for arranging pairs adjacent to each other
Trapping Rain Water 
Convert array into Zig-Zag fashion
Find maximum average subarray of k length  
Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed  
Reorder an array according to given indexes  
Find zeroes to be flipped so that number of consecutive 1’s is maximized  
Count triplets with sum smaller than a given value  
Find the subarray with least average  
Count Inversions of size three in a give array
Longest Span with same Sum in two Binary arrays
Merge two sorted arrays with O(1) extra space
Form minimum number from given sequence
Subarray/Substring vs Subsequence and Programs to Generate them
Count Strictly Increasing Subarrays
Rearrange an array in maximum minimum form
Find minimum difference between any two elements
		Sort the First Array and then Iterate over the other to find the Minimum difference 

Find lost element from a duplicated array 

Count pairs with given sum
	Insert first Array inside a unordered_set and traverse the second one to find if diff/sum is present in the hash set... 

Count minimum steps to get the given desired array
Find minimum number of merge operations to make an array palindrome
Minimize the maximum difference between the heights
Find the Rotation Count in Rotated Sorted array
	**************** Find Index of the Minimum Number
	**************** check if mid == lowest Number 
	**************** check if mid+1 is the lowest number 
	**************** check if low == high 
	**************** check if high > mid 
			**************** search in left parts 
				else
			**************** search in right parts 

Binary Search tree 
	Height is a Binary Search Tree ....
		int left = findDepth(root->left);
		int right = findDepth(root->right);


Object Pool ************ DONE *********************

Adjacency List 
Concurrent Queue 
Celebrity Problem 
Connection Pool 
BFS --- Breadth First Search 

Count ways to reach the n’th stair
	ways(n) can be either ways(n-1) + ways(n-2) .....
	countways(n){
		if n <= 1
			return n;
		else
			return countways(n-1) + countways(n-2); 
	}

	countWays(size, numberSteps)
	{
		if( n <= 1)
			return n;

		int result = 0;
		for( int i = 0 ; i <= numberSteps && i <= n; i++)
			res += countways(n-i, numberSteps);
	}

	using a Stack 
			Push all the Persons inside the Stack ....
			Create a 2 dimension Array MATRIX[N][N]

			int C ; 

			for( auto i : vector )
				stack.push(i);

			Pop top 2 elements from Stack and check

			int A = stack.top();
			stack.pop();

			int B = stack.top();
			stack.pop();

			while ( stack size > 1)
			{
			
				if( MATRIX [FIRST][SECOND] ) // If A Knows B
					Then A Cannot be a Celebrity
					stack.push(B) 

				if( MATRIX [SECOND][FIRST] ) // If B knows A
					Then B cannot be a Celebrity
					stack.push(A) 
			}

			C = stack.top();

			s.pop();

			if( knows(C, A) )
				C = A;

			if( knows(C, B ) )
				C = B;

Interleave the first half of the queue with second half 

/* Get minimum element from stack  */
Create a specialized Stack that contains Stack and where only the minElement is stored ..... 

/* Given an array and an integer k, find the maximum for each and every contiguous subarray of size k. */ 

/*** Transform one word into Another ***/
int minOperations(string& s1, string& s2)
{
	if( s1.size() != s2.size() )
		return;

	for( auto i, s1)
		countS1[s1[i]++];

	for( auto j : s2 )
		countS1[s2[j]--];

	for( auto i : i < 256 )
		if countS1[i] 
			return;

	for( int i = s1.size() - 1, j = s2.size() - 1 ; i >= 0 )
	{
		while( s2[i] != s1[j] )
		{
			i--;
			res++
		}

		if( i >= 0 )
			j--;
			i--;

	}

	return res; 



	}

}




 vector< vector<int> > subarray;
for(int start=0; start<array.size(); start++)
{
    for(int end=0; end<array.size(); end++)
    {
        vector<int> sub;
        for(int i=start; i<=end; i++)
        {
            sub.push_back(array[i]);
        }
        subarray.push_back(sub);
        sub.clear();
    }
}



vector<int> arr = { 1, 2, 3, 2, 3, 4, 4, 5, 1, 1, 5, };

vector<vector<int> > subArray;
for( int start = 0 ; start < array.size(); ++start )
{
	for( int end = 0 ; end < array.size(); ++end )
	{
		vector<int> sub;
		for( int i = start; i <= end; ++i )
		{
			sub.push_back(array[i];
		}
		
		subArray.push_back(sub);
		sub.clear();
}

for( auto var: subArray )
{
	cout << var << endl;
}

int findShortestSubArray(vector<int>& nums) {
        map <int,int> r,l,cnt;//three maps for left index, right index and count
        for(int i=0;i<nums.size();++i) {
            int x=nums[i];
            if(!l[x]) l[x]=i+1;//i+1 for the case where max frequency element resides in index 0.
            r[x]=i+1,cnt[x]++;
        }
        int m=INT_MIN,size=INT_MAX;
        map<int,int> :: iterator it;
        
        for(it=cnt.begin();it!=cnt.end();++it) 
            m=max(m,it->second);//getting degree of the array
        
        for(it=cnt.begin();it!=cnt.end();++it) {
            if(it->second == m) {//the maximum occurring element
                size=min(size,r[it->first]-l[it->first]+1);//get the size of the subarray and keep track of the minimum
            }
        }
        return size;
    }

int findShortestPath(vector<int>& arr) {
                map<int,int> left;
                map<int,int> right;
                map<int,int> count_map;
                
                for(int i=0; i <arr.size();i++) {
                                count_map[arr[i]]++;
                                if(left.find(arr[i]) == left.end()) {
                                                left[arr[i]] = i;
                                }
                                right[arr[i]] = i;
                }
                
                int ans = arr.size();
                
                int degree = 0;
                for(auto item:count_map) {
                                degree = max(degree,item.second);
                }
                
                for(auto val: count_map) {
                                if(count_map[val.first] == degree) {
                                                ans = min(ans,right[val.first] - left[val.first] + 1);
                                }
                }
                cout << ans << endl;
                return 0;
}

Input: [1,2,2,3,1,4,2]
Output: 6

2 unordered_maps
	One records the starting index of the Element
	Second records the Frequency of an Element
	
	unordered_map<int, int> count;
	unordered_map<int, int> index;
	
	int len = vec.size();
	int frequency = 0;
	
	for (int i = 0 ; i < vec.size(); ++i )
	{
		if(index.count(vec[i]) == 0 )
			index[num[i]] = i;
		
		count[num[i]]++;
		
		if(count[num[i]] == degree )
		{
			len = min(i - index[num[i]] + 1, len);
		}
		
		if( count[num[i]] > degree )
		{
			len = i - index[num[i]] + 1;
			degree = count[num[i]];
		}
		
	}
	
	return len;
	
	unordered_map<int, vector<int> > myMap;
	for( int i = 0 ; i < vec.size(); ++i )
		myMap[vec[i]].push_back(i);
		
	// Find Max Degree
	for( auto it = myMap.begin(); it != myMap.end(); ++it)
		degree = max(degree, it->second.size());
		
	// Find the Shortest Degree
	for( auto it = myMap.begin(); it != myMap.begin(); ++it)
	[
		if( it->second.size() == degreee
			shortest = min(shortest, it->second.back() - it->second[0]+1 )
	
	
	Since the advent of non-blocking-io, there is very few reason to create truly multi-threaded application. Employ pattern like GCD (Grand Central Dispatch), where various non-blocking-io completion events happen from a single thread
	
#include <iostream>
#include <vector>
using namespace std;
 
int main() {
	// your code goes here
	vector<int> arr = { 1, 2, 1};
 
	vector<vector<int> > subArray;
	for( int start = 0 ; start < arr.size(); ++start )
	{
		for( int end = 0 ; end < arr.size(); ++end )
		{
			vector<int> sub;
			for( int i = start; i <= end; ++i )
			{
				sub.push_back(arr[i]);
				//cout << arr[i] << endl;
			}
 
			if( sub.empty() )
				continue; 
 
			subArray.push_back(sub);
 
			// cout << endl;
			sub.clear();
		}
	}
 
	int degree = 0 ;
	cout << "Number of Sub-Arrays = " << subArray.size() << endl; 
	for( int i = 0 ; i < subArray.size(); ++i )
	{
		// cout << var.size() << endl;
		vector<int> temp = subArray[i];
		for( int j = 0 ; j < temp.size(); ++j)
			cout << temp[j] << " - ";
 
		cout << endl;
	}	
 
	return 0;
}	

#include <iostream>
#include <string>

using namespace std;

string removeDuplicates(string str, int size)
{
	int k = 0;
	
	for( int i = 1; i < size; ++i )
	{
		if( str[i-1] != str[i] )
			str[k++] = str[i-1];
		else
		{
			while( str[i-1] == str[i] )
			{
				i++;
			}
	}
	
	str[k++] = str[i-1];
	
	if( k != size )
		removeDuplicates(str, k );
	else	
		return str;
}
		

/* Sum of all prime numbers between 1 and N. ..... */

Apply Sieve of Erasthoses Theorem to find all Prime Numbers till N..

for( int k = 2; k*k < n; ++k)
{
	if( arr[k] == true)
	{
		for( int j = k*2; j < n ; j = j+k)
		{
			arr[j] = false;
		}
	}
}



/******* Find contigious sub array with given sum *********/

unordered_map<int, int>

int currentSum;

for( auto i: vector)
{
	currentSum += vector[i];
	if(currentSum == sum )
		cout << "Found";
		
	if( map[currentSum - sum] != end )
		cout << "found";
		
	map[currentSum] = i;
	
/** SAMPLE INPUT/OUTPUT CODE **/

int main() {
    int t;
    cin >> t; // Number of Test Cases
    for(int a0 = 0; a0 < t; a0++){
        int n; // Size of Vector
        int k; // Threshhold to check ..
        cin >> n >> k;
        vector<int> a(n); // Input Vector of Ints ....
        for(int a_i = 0; a_i < n; a_i++){
           cin >> a[a_i];
        }
        string result = angryProfessor(k, a);
        cout << result << endl;
    }
    return 0;
}

********************************************************************************************************************
Snake and Ladder Problem

********************************************************************************************************************
Chocolate Distribution Problem
	Choc Packets with variable number of chocolates.....
	Distribute in such a way that diff between Packet with Max chocolates and Packet with Min chocolates in minimum.
	Classic sub-set problem..
	
	Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} 
        m = 5
	Output: Minimum Difference is 6
	The set goes like 3,4,7,9,9 and the output 
	is 9-3 = 6
	
	Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41,
                 30, 40, 28, 42, 30, 44, 48, 
                 43, 50}
	Students = 7 ... Output = 10 ....
	Find All sub-set of 7 and find the one that has minimum diff between Min and Max values in it... 
	Sort and find sub-set of 7 and choose....
	
	Boundary Cases .....
	Students Cannot be more than Packets ... Students cannot be zero or Chocolates cannot be zero .....
	sort the Array...
	int first = last = 0;
	int min_diff = INT_MIN;
	
	for( int i = 0 ; i + students - 1 < numberOfPackets; ++i )
	{
		min_diff = arr[i + stud - 1 ] ( Maximum ) - arr[i];
		if( diff < min_diff )
		{
			min_diff = diff;
			first = arr[i];
			last = arr[i + students - 1 ];
		}
	}
	return ( arr[first], arr[last] );
	
********************************************************************************************************************
	
Solve the Sudoku
Shortest direction
0 – 1 Knapsack Problem
Inversion of array
Maximum of all subarrays of size k
Possible words from Phone digits

Doubling the value
	......
	Apply Binary Search ... First sort the Array.
	Check if given B is less than max values of the Array.
		if less, binary search element in the array.
			if 
				Found - b = b * 2;
			else
				return b;
	}
	
Print the Kth Digit
Consecutive 1’s not allowed
Search in a Rotated Array
Kadane’s Algorithm
Rat in a Maze Problem
Multiply two strings
Expression Tree
LRU Cache
	get(key) --> return value or return -1 ...
	put(key, value) --> Insert it into the cache if there are free space available
					--> If No free Space is available, free the least used key
					--> Insert this in it's place ...
					
					class LRUCache{
						int _capacity;
						
						// Store reference of list in the cache
						unordered_map<int, list<int>::iterator> _cache;
						
						// Using list as a double ended Queue ... 
						list<int> iQueue;			// Most Recently used will be placed in near front end ...
													// Least recently will be placed near the rear end ...
						public:
							explicit LRUCache(int capacity) : _capacity(capacity);
							
							int get(int key);
							
							void put(int key, int value);
					};
					
					void LRUCache::put(int value)
					{
						if( _cache.find(value) == _cache.end() ) // Value not Found
						{
							if( iQueue.size() == _capacity ) // We need to free some Space to insert the Element
							{
								int last = iQueue.back();
								iQueue.pop_back();
								_cache.erase(last);
								
							}
						}
						else
						{
							// Erase it from the list
							// and Insert it into the beginning of the list
							_cache.erase(value);
						}
						
						iQueue.push_front(value);
						_cache[value] = iQueue.begin();
					}
					
					int LRUCache::get(int key)
					{
						if( _cache.find(key) != end )
						{
							int val = _cache[key].begin() ;
							// Remove this from end of the list and place it in the beginning
							iQueue.pop_back();
							iQueue.push_front(val);
							
							_cache[va] = iQueue.begin();							
						}
						else
							return -1;
					}
					
Serialize and Deserialize a Binary Tree
Get minimum element from stack
Print a Binary Tree in Vertical Order
Topological sort
The Celebrity Problem
Print BST elements in given range
Detect cycle in an undirected graph
Detect cycle in a directed graph
Queue using two Stacks
Flattening a Linked List
Connect Nodes at Same Level
Delete Middle of Linked List
Finding middle element in a linked list
Bottom View of Binary Tree

******************************************************************************************************

Diff Between 
	Largest Contiguos Palindrome String AND
	Largest Palindrome Sstrin
	
void findAllPalinromicString(string str)
{
	for(int i = 0 ; i <str.length(); ++i)
	{
		// Find all odd number of Palindromes
		expand(i, i, str, mySet);
		
		expand(i, i+i, str, mySet);
	}
}

void expand(int low, int high, string str, set<string> mySet )
{
	while( low >= 0 && high <= str.length() && str[low] == str[high] )
		mySet.isert( str.substr(low, high - low + 1)
		--low;
		++high
}

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
