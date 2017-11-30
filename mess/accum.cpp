#include <iostream>
#include <numeric>
#include <vector>
#include <functional>

using namespace std;

#define MAX 10
vector<long> v(MAX);

int main()
{
	// Fill vecctor using conventional loop
	//
	for(int i=0; i<MAX; ++i)
		v[i] = i+1;

	// Accumulate the sum of contained values
	// 
	long sum = accumulate(v.begin(), v.end(), 0);
	cout << "Sum of values == " << sum << endl;

	// Accumulate the product of contained values
	//
	long product = accumulate(v.begin(), v.end(), 1, multiplies<long>());
	cout << "Product of values == " << product << endl;

	return 0;
}