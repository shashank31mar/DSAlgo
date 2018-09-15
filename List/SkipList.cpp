#include <iostream>
#include <vector>
#include <limits>
#include <stdlib.h>
#include <time.h>

using namespace std;

struct SkipNode {

	SkipNode(string key, int data)	 {
		this->data = data;
		this->key = key;
		this->left = NULL;
		this->right = NULL;
		this->up = NULL;
		this->down = NULL;
	}
	
	string key;
	int data;
	int pos;
	vector<int> width;
	SkipNode* left;
	SkipNode* right;
	SkipNode* up;
	SkipNode* down;
};

class SkipList {
	public:
		SkipList():_head(NULL) {
			_head = new SkipNode(numeric_limits<string>::min(),0);
			_tail = new SkipNode(numeric_limits<string>::max(),0);

			_head->right = _tail;
			_tail->left = _head;

			_height = _nodes = 0;
			srand (time(NULL));
		}
		
		void insert(const string& aKey, const int& aData) {
			insertUtil(aKey, aData);
		}
	
		void remove(const string& aKey) {
			SkipNode* aNode = findKey(aKey);
			SkipNode* p;

			if (aNode->key.compare(aKey) != 0) {
				return ;
			}

			while (aNode != NULL) {

				aNode->left->right = aNode->right;
				aNode->right->left = aNode->left;

				p = aNode->up;
				delete(aNode);
				aNode = p;
			}
		}
		
		const SkipNode* get(const string& aKey) {
			SkipNode* aNode = findKey(aKey);

			if (aNode->key.compare(aKey) == 0) {
				return aNode;
			}
			else {
				cout << "Key not Found!!" << endl;
				return NULL;
			}
		}

		SkipNode* findKey(const string& aKey) {
			SkipNode* aNode = _head;
			return findKeyUtil(aKey, aNode);
		}
		
		bool isEmpty() {
			return (_nodes == 0);
		}

		void print(const SkipNode* aNode) {
			if (aNode == NULL) {
				cout << "Node is NULL!!" << endl;
			}
			else {
				cout << "Node key : " << aNode->key << " ==> Node Value : " << aNode->data << endl;
				cout << "Node Width : ";
				for (int i=0; i < aNode->width.size(); i++) {
					cout << aNode->width[i] << " ";
				}
				cout << endl;
			}
		}

		void printHorizontal() {
			SkipNode* aNode;
			string s = "";
			int i = 0;

			aNode = _head;

			while (aNode->down != NULL) {
				aNode = aNode->down;
			}

			while ( aNode != NULL) {
				aNode->pos = i++;
				aNode = aNode->right;
			}

			aNode = _head;

			while (aNode != NULL) {
				s = getOneRow(aNode);
				cout << s << endl;
				aNode = aNode->down;
			}
		}

		void printVertical() {
			string s = "";

			SkipNode* aNode;

			aNode = _head;

			while (aNode->down != NULL) {
				aNode = aNode->down;
			}

			while (aNode != NULL) {
				s = getOneColumn(aNode);
				cout << s << endl;

				aNode = aNode->right;
			}
		}

		const int getHeight() const {
			return _height;
		}
	private:
		const int getRandom() const {
			return rand()%2;
		}

		void insertUtil(const string& aKey, const int& aData) {
			SkipNode* p, *q;
			p = findKey(aKey);

			if (aKey.compare(p->key) == 0) {
				p->data = aData;
				return;
			}

			q = new SkipNode(aKey, aData);

			q->left = p;
			q->right = p->right;
			p->right->left = q;
			p->right = q;
				
			int i = 0;

			q->width.push_back(1);

			while (getRandom()) {
				if (i >= _height) {
					SkipNode* p1 = new SkipNode(numeric_limits<string>::min(),0);
					SkipNode* p2 = new SkipNode(numeric_limits<string>::max(),0);

					p1->right = p2;
					p2->left = p1;

					p1->down = _head;
					_head->up = p1;

					p2->down = _tail;
					_tail->up = p2;

					_head = p1;
					_tail = p2;
					
					_height++;
				}

				int levelWidth = 1;

				while(p->up == NULL) {
					p = p->left;
					levelWidth++;
				}

				p = p->up;

				SkipNode* e = new SkipNode(aKey,aData);

				// Initializing links for e
				e->left = p;
				e->right = p->right;
				e->down = q;

				int x=0;
				for(x=0; x < q->width.size(); x++) {
					e->width.push_back(q->width[x]);
				}

				e->width.push_back(levelWidth);
				// Initializing neighbouring links

				p->right->left = e;
				p->right = e;
				q->up = e;

				q = e;

				i++;
			}

			_nodes++;
		}

		SkipNode* findKeyUtil(const string& aKey, SkipNode* aNode) {
			while(true) {
				while(((aNode->right->key) != numeric_limits<string>::max()) && aNode->right->key.compare(aKey) <= 0) {
					aNode = aNode->right;
				}
				if (aNode->down != NULL) {
					aNode = aNode->down;
				}
				else {
					break;
				}
			}
			return aNode;
		}

		const string getOneRow(SkipNode* aNode) {
			string s = "";
			SkipNode* q;
			int a,b,i;

			a = 0;
			s = "" + aNode->key;
			aNode = aNode->right;

			while (aNode != NULL) {
				q = aNode;

				while (q->down != NULL) {
					q = q->down;
				}

				b = q->pos;

				s = s + " <-";

				for (i = a+1; i < b ; i++) {
					s = s + "------";
				}

				s = s + "> " + aNode->key;

				a = b;

				aNode = aNode->right;
			}

			return s;
		}

		const string getOneColumn(SkipNode* aNode) {
			string s = "";

			while(aNode != NULL) {
			    s = s + " " + aNode->key;

			    aNode = aNode->up;
			}

			return s;
		}

		SkipNode* _head;
		SkipNode* _tail;
		int _height;
		int _nodes;
};

int main() {
	SkipList* aList = new SkipList();

	aList->insert("CA",1);
	
	aList->insert("C",1);
	
	aList->insert("2",1);
	
	aList->insert("3",1);
	
	aList->insert("4",1);
	
	aList->insert("5",1);
	
	aList->insert("6",1);
	
	aList->insert("7",1);
	
	aList->insert("8",1);
	
	aList->insert("9",1);
	
	aList->insert("D",1);
	
	aList->insert("E",1);
	
	aList->insert("A",1);
	
	aList->insert("B",1);
	
	aList->printHorizontal();
	
	aList->print(aList->get("4"));

	cout << "Removing element with Key 7" << endl;
	aList->remove("7");

	aList->printHorizontal();
	
	return 0;
	
	
	//Visual explanation http://w...content-available-to-author-only...y.edu/~cheung/Courses/323/Syllabus/Map/skip-list-impl.html#newlayer
}