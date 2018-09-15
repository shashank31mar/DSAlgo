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

void mirrorInorderTraversal(Node* node) {
	
	if (node == NULL) 
		return;
		
	mirrorInorderTraversal(node->right);
	cout << node->data << " ";
	mirrorInorderTraversal(node->left);
}

void InorderTraversal(Node* node) {
	
		if (node == NULL) 
		return;
		
	InorderTraversal(node->left);
	cout << node->data << " ";
	InorderTraversal(node->right);
}

void mirrorTree(Node* node) {
	if(node == NULL) {
		return;
	}
	
	mirrorTree(node->left);
	mirrorTree(node->right);
	
	Node* tmp = node->right;
	node->right = node-> left;
	node->left = tmp;
}

int main() {

	Node* n = new Node(8);
	n->left = new Node(4);
	n->right = new Node(10);
	
	n->left->right =  new Node(6);
	n->left->right->right = new Node(7);
	n->left->right->left = new Node(5);
	
	n->left->left = new Node(2);
	n->left->left->right = new Node(3);
	n->left->left->left = new Node(1);
	
	n->right->right = new Node(11);
	n->right->left = new Node(9);
	
	InorderTraversal(n);
	cout << endl;
	
	mirrorInorderTraversal(n);
	cout << endl;
	
	mirrorTree(n);
	
	mirrorInorderTraversal(n);
	

	return 0;
}