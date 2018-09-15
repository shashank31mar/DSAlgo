#include <iostream>
#include <vector>
#include <list>
using namespace std;

class Node {
	
public:
	Node(): _visited(false), _data("") {
		
	}
	
	string getData() {
		return _data;
	}
	
	void setData(string iData) {
		_data = iData;
	}
	
	bool isVisited() {
		return _visited;
	}
	
	void setVisited(bool iVisited) {
		_visited = iVisited;
	}
	
	vector<Node*> getNeighbours() {
		return _neighbours;
	}
	
	void setNeighbours(Node* node) {
		_neighbours.push_back(node);
	}
	
private:
	bool _visited;
	string _data; 
	vector<Node*> _neighbours;
};

class Graph {
	
public:
	Graph(int size) : _n1(NULL), _n2(NULL) {
		//_graph.resize(size);
	}
	
	void DFSUtility(Node* startNode) {
		if(startNode == NULL)
			return;
			
		if(!startNode->isVisited()) {
			
			startNode->setVisited(true);
			cout << startNode->getData() << " ";
			
			for(auto neighbour: startNode->getNeighbours()) {
				DFSUtility(neighbour);
			}
			
		}
	}
	
	void DFS(string node) {
		DFSUtility(search(node));
		
	}
	
	void BFSUtility(Node* node) {
		list<Node*> queue;
		
		queue.push_back(node);
		node->setVisited(true);
		cout<< node->getData() << " ";
		
		while(!queue.empty()) {
			Node* n = queue.front();
			queue.pop_front();
			for(auto node : n->getNeighbours()) {
				if(!node->isVisited()) {
					node->setVisited(true);
					queue.push_back(node);
					cout << node->getData() << " ";
				}
			}
		}
	}
	
	void BFS(string node) {
		BFSUtility(search(node));
	}
	
	Node* search(string data) {
		//cout << "inside search" << endl;
		for(auto node : _graph) {
			if(node->getData() == data){
				//cout<< "data is : " << node->getData() <<endl;
				return node;
			}
		}
	}
	
	void addVertex(string n1) {
		Node* node = new Node();
		node->setData(n1);
		_graph.push_back(node);
		//cout << node->getData() << endl;
	}
	
	void addEdge(string n1, string n2) {
		_n1 = search(n1);
		_n2 = search(n2);
		
		_n1->setNeighbours(_n2);
		_n2->setNeighbours(_n1);
	}
	
	void resetGraph() {
		for(auto node: _graph) {
			node->setVisited(false);
		}
		
		cout << endl;
	}
	
private:
	vector<Node*> _graph;
	Node* _n1;
	Node* _n2;
};


int main() {
	
	Graph* graph = new Graph(5);
	
	graph->addVertex("paris");
	graph->addVertex("london");
	graph->addVertex("nice");
	graph->addVertex("barcelona");
	graph->addVertex("rome");
	
	graph->addEdge("paris", "london");
	graph->addEdge("paris", "nice");
	graph->addEdge("london", "barcelona");
	graph->addEdge("barcelona", "nice");
	graph->addEdge("nice", "rome");
	graph->addEdge("rome", "paris");
	
	graph->DFS("paris");
	graph->resetGraph();
	graph->BFS("nice");
	
	return 0;
}