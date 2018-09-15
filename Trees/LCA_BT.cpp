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

Node* findLCA(Node* root, int n1, int n2) {
	
	if(root == NULL) {
		return NULL;
	}
	
	if(root->data == n1 || root->data == n2) {
		return root;
	}
	
	Node* left_lca = findLCA(root->left, n1, n2);
	Node* right_lca = findLCA(root->right, n1, n2);
	
	//case where nodes are present in left and right subtree
	if(left_lca && right_lca) {
		return root;
	}
	
	//case where both the node are in same sub tree
	return (left_lca != NULL) ? left_lca:right_lca;
}

int main() {

Node* root = new Node(1);
	root->left = new Node(2);
	root->right = new Node(3);
	
	root->left->left = new Node(4);
	root->left->right = new Node(5);
	
	root->right->left = new Node(6);
	root->right->left->right = new Node(7);
	
	cout << "LCA is : " << findLCA(root, 6,7)->data << endl;
	cout << "LCA is : " << findLCA(root, 1,7)->data << endl;
	cout << "LCA is : " << findLCA(root, 5,7)->data << endl;
	
	return 0;
}