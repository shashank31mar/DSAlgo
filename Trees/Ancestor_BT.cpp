#include <iostream>
using namespace std;

struct Node {
	
	Node(int data) : left(NULL), right(NULL) {
		this->data = data;
	}	
	
	int data;
	Node* left;
	Node* right;
};

bool findAncestor(Node* root, int target) {
	if(root == NULL) {
		return false; 
	}
	
	if(root->data == target) {
		return true;
	}
	
	if(findAncestor(root->left, target) || findAncestor(root->right, target)) {
		cout << root->data << endl;
		return true;
	}
}

int main() {

	Node* root = new Node(1);
	root->left = new Node(2);
	root->right = new Node(3);
	
	root->left->left = new Node(4);
	root->left->right = new Node(5);
	
	root->right->left = new Node(6);
	root->right->left->right = new Node(7);
	
	findAncestor(root, 7);
	
	
	
	return 0;
}