#include <iostream>
#include <list>
#include <unordered_map>


//dont use ordered map duplicate keys willnot be entered into the map, so the output is wrong
//logic is correct
using namespace std;

struct Node {
	Node(int data) {
		this->data = data;
	}
	
	int data;
	int height;
	Node* left;
	Node* right;
};

void bottomView(Node* root) {
     if(root == NULL) 
         return;
         
     int ht = 0;
     
     unordered_map<int, int> hash;
     
     list<Node*> list;
     
     root->height = ht;
     
     list.push_back(root);
     
     while(!list.empty()) {
         Node* node =  list.front();
         list.pop_front();
         
         ht = node->height;
         
         pair<int, int> data(ht, node->data);
         
         hash.insert(data);
         
         if(node->left != NULL) {
             node->left->height = ht -1;
             list.push_back(node->left);
         }
         
         if(node->right != NULL) {
             node->right->height = ht + 1;
             list.push_back(node->right);
         }
     } 
     
	for(auto i : hash) {
		cout << " key is : " << i.first << " and value is : " << i.second << endl;
	}
 }
 
int main() {
	
	Node* n = new Node(8);
	n->left = new Node(4);
	n->right = new Node(10);
	
	n->left->left = new Node(2);
	n->left->right =  new Node(6);
	
	n->right->left = new Node(9);
	n->right->right = new Node(11);
	
	n->left->right->right = new Node(7);
	n->left->right->left = new Node(5);
	
	
	n->left->left->right = new Node(3);
	n->left->left->left = new Node(1);
	
	n->right->right = new Node(11);
	n->right->left = new Node(9);
	
	bottomView(n);
	return 0;
}