#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

double darray[10] = {1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9};

vector<double> vdouble(10);

int main(){
	vector<double>::iterator outputIterator = vdouble.begin();
	copy(darray, darray + 10, outputIterator);
	replace(vdouble.begin(), vdouble.end(), 1.5, 1.5111);
	reverse(vdouble.begin(), vdouble.end());
	random_shuffle(vdouble.begin(), vdouble.end());
	while (outputIterator != vdouble.end()) {
		cout << *outputIterator << endl;
		outputIterator ++;
	}
	return 0;
}