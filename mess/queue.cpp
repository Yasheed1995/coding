#include <iostream>
#include <queue>

using namespace std;
int main() {
	priority_queue<int> mypq;
	priority_queue<int> hh;	
	mypq.push(39);
	mypq.push(45);
	mypq.push(23);
	mypq.push(384);
	mypq.swap(hh);
	for (int i=0; i<5;++i) mypq.push(i);
	cout<< "Popping out elements...";
	while (!mypq.empty()){
		cout<< ' ' << mypq.top();
		mypq.pop();
	}

	cout<<'\n';
	cout<<mypq.size()<<endl;
	return 0;
}
