#include <vector>
#include <algorithm> 
#include <iostream>

using namespace std;

struct greater1{
	bool operator()(const int &a, const int &b) const {
		return a > b;
	}
};

int main(){
	vector<int> hh;
	hh.push_back(34);
	hh.push_back(348);
	hh.push_back(8);
	hh.push_back(23);

	make_heap(hh.begin(),hh.end(),greater1());
/*	while(hh.size()){
		pop_heap(hh.begin(),hh.end(),greater1());
		int min = hh.back();
		hh.pop_back();
		cout<< min << endl;
	}*/
	for(vector<int>::iterator it = hh.begin();it!=hh.end();++it){
		cout<<*it<<endl;
	}
	cout<<hh.size()<<endl;
return 0;
}
