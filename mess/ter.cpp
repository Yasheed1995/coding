#include<iostream>

using namespace std;

class Node {
friend class MyList;
public: 
	Node(): n(0),prev(NULL), next(NULL) { }
	Node(int _n) : n(_n),prev(NULL), next(NULL) { }
	
private: 
	int n;
	Node* prev;
	Node* next;
};

class MyList 
{	
public:
	MyList(){
		dummy.prev = &dummy;
		dummy.next = &dummy;
	}
	void pushFront(int _n) {
		Node* p = new Node(_n);
		p->next = dummy.next;
		
		dummy.next->prev = p;
		dummy.next = p;
		p->prev = &dummy;
}
	friend ostream& operator<< (ostream& o, const MyList& list){
		list.print(o);
		return o;
}
protected:
	void print(ostream& o) const {
		Node *p = dummy.next;

		while (p->next != &dummy) {
			o<<p->n<<"->";
			p = p->next;
			
}
		o << "NULL" <<endl;	
}
private:
	Node dummy;	
};

int main() {

	}
