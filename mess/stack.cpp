#include <iostream>
#include <list>

using namespace std;

int main(){
	list<int> ll;
	ll.push_back(2);
	ll.push_back(3);
	ll.push_back(4);

	for( list<int>::iterator it = ll.begin(); it!=ll.end(); ++it){
		cout << *it << endl;
}
	return 0;
}

