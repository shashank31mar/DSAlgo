/*
 * SegmentTree.cpp
 *
 *  Created on: 19-May-2015
 *      Author: shashankgupta
 */

//Reference
//http://se7so.blogspot.in/2012/12/segment-trees-and-lazy-propagation.html

//Sum of a given range in an array
#include <iostream>
#include <vector>

using namespace std;

struct STNode {
	STNode() {
		data = -999999;
		left = NULL;
		right = NULL;
		low_range = -1;
		high_range = -1;
	}
	
	STNode(int data) {
		this->data = data;
		left = NULL;
		right = NULL;
		low_range = -1;
		high_range = -1;
	}

	int data;
	STNode* left;
	STNode* right;
	int low_range;
	int high_range;
};

class SegmentTree {
public:
	SegmentTree() :
			_root(NULL) {

	}

	STNode* buildTree(STNode* root, vector<int>& arr, int low_range,
			int high_range) {

		if (low_range > high_range || low_range < 0
				|| high_range > arr.size()-1) {
					cout<<"here"<<endl;
			return NULL;
		}
		
		if(!root) {
			//cout << "here too" << endl;
			root = new STNode();
		}
		
		//leaf case
		if (low_range == high_range) {
			root->data = arr[low_range];
			root->low_range = low_range;
			root->high_range = high_range;
			//cout << "current node data is : " << root->data << endl;
			return root;
		}

		int mid = low_range + (high_range-low_range)/2;

		//Set Left Child
		root->left = buildTree(root->left, arr, low_range, mid);
		
/*		cout<< "low range is : " << low_range << " high Range is : " << high_range << " mid is : " << mid << endl;
		
		cout<< "left child is : " << root->left->data 
			<< "low range is : "<< root->left->low_range 
			<< " high range is : "<< root->left->high_range 
			<< endl;
			
		cout << "root data is : " << root->data << endl;*/
		
		//Set Right Child
		root->right = buildTree(root->right,arr, mid+1, high_range);

/*		cout<< "right child is : " << root->right->data 
			<< "low range is : "<< root->right->low_range 
			<< " high range is : "<< root->right->high_range 
			<< endl;


		cout<< "before sum, left child is : " << root->left->data 
			<< "right child is : "<< root->right->data 
			<< endl;*/
		//Set Root
		root->data = root->left->data + root->right->data;
		root->low_range = low_range;
		root->high_range = high_range;
		
/*			cout<< "After sum, root is : " << root->data 
			<< "low range is : "<< root->low_range 
			<< " high range is : "<< root->high_range 
			<< endl << endl;*/

		return root;
	}

	int search(int low_index, int high_index) {
		if(low_index > high_index || _root->low_range > high_index || _root->high_range < low_index) {
			return -999999;
		}
		return searchUtil(_root,low_index, high_index);
	}

	void update(int old_value, int new_value, int value_index) {
		if(_root == NULL) {
			cout << "tree is empty, sorry can't update!!" << endl;
			return;
		}
		
/*		if(low_index > old_value_index || high_index < old_value_index) {
			cout << "Index value out of range!!" << endl;
			return;
		}*/
		
		updateUtil(_root, new_value-old_value, value_index, _root->low_range, _root->high_range);
	}

	void printSegmentTree() {
		printSegmentTreeUtil(_root);
		cout<<endl;
	}

	void setRoot(STNode* root) {
	//	cout<<root->data<<endl;
		_root = root;
	}

private:
	int searchUtil(STNode* root, int low_index, int high_index) {
		int sum=0;
		if(root == NULL) {
			return 0;
		}
		
		if(root->low_range >= low_index &&  root->high_range <= high_index) {
			return root->data;	
		}
		if(root->low_range > high_index || root->high_range < low_index)
			return 0;
			
		return searchUtil(root->left,low_index,high_index) + searchUtil(root->right,low_index,high_index);
	}

	void updateUtil(STNode* root, int diff, int value_index, int low_index, int high_index) {
		if(root == NULL) {
			//cout << "Tree is empty, can't update it!!" << endl;
			return ;
		}
		
		if(value_index < low_index || value_index > high_index) {
			return;
		}
		
		 root->data += diff;
		
		int mid = low_index + (high_index-low_index)/2;
		
		updateUtil(root->left, diff, value_index, low_index, mid);
		updateUtil(root->right, diff, value_index,mid+1, high_index);
	}

	void printSegmentTreeUtil(STNode* root) {
		if(root == NULL) {
		//	cout<< "Nothing to print,tree is empty!!" << endl;
			return;
		}

		printSegmentTreeUtil(root->left);
		cout<< root->data << " ";
		printSegmentTreeUtil(root->right);
	}

	STNode* _root;
};

int main() {
	vector<int> arr = {2,4,-6,8,9,10,11};
	STNode* root;

	SegmentTree st;

	root = st.buildTree(root,arr,0, arr.size()-1);
	st.setRoot(root);

	st.update(-6,-8,2);	//update value -6 with -8 at index 2
	cout << "Sum is : " << st.search(1,5) <<endl;	//sum between 0-6
	//st.printSegmentTree();

	return 0;
}
