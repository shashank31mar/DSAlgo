#include <iostream>
#include <vector>
using namespace std;


class Heap {

public:
	Heap() {
		
	}
	
	void insert(int data) {
		heap.push_back(data);
		heapifyUP(heap.size() -1);
	}
	
	int deleteMin() {
		int min = heap.front();
		
		heap[0] = heap.at(heap.size()-1);
		
		heap.pop_back();
		
		heapifyDown(0);
		
		return min;
	}
	
	void print() {
		for(auto item: heap) {
			cout << item << " ";
		}
		
		cout << endl;
	}
	
private:
	int left(int parent) {
		return 2*parent;
	}
	
	int right(int parent) {
		return 2*parent + 1;
	}
	
	int parent(int child) {
		return child/2;
	}
	
	void heapifyUP(int index) {
		
		while(index > 0 && parent(index) >= 0 && ( heap[parent(index)] > heap[index] ) ) {
			int tmp =  heap[parent(index)];
			heap[parent(index)] = heap[index];
			heap[index] = tmp;
			
			index = parent(index);
		
		}
	}
	
	void heapifyDown(int index) {
		
		int child = left(index);
		
		if(child > 0 && right(index) > 0 && ( heap[child] > heap[right(index)] ) ) {
			
			child = right(index);
		}
		
		if(child > 0) {
			int tmp = heap[index];
			heap[index] = heap[child];
			heap[child] = tmp;
			heapifyDown(child);
		}
		
	}
	
	vector<int> heap;
};

int main() {
	
	Heap* minHeap =  new Heap();
	
	minHeap->insert(20);
	minHeap->print();
	minHeap->insert(670);
	minHeap->print();
	minHeap->insert(30);
	minHeap->print();
	minHeap->insert(10);
	minHeap->print();
	minHeap->insert(2);
	minHeap->print();
	minHeap->insert(245);
	minHeap->print();
	minHeap->insert(15);
	minHeap->print();
	minHeap->insert(20);
	minHeap->print();
	minHeap->insert(4);
	minHeap->print();

	return 0;
}