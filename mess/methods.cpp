#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>

using namespace std;

#define VSIZE 48
vector<long> v(VSIZE);

// Function prototypes
void initialize(long &ri);
void show(const long &ri);
bool isMinus(const long &ri); // Predicate func

int main()
{
	srandom( time(NULL) ); // Seed random generator

	for_each(v.begin(), v.end(), initialize);
	cout << "Vector of signed long integers" << endl;
	for_each(v.begin(), v.end(), show);
	cout << endl;

	// Use predicate function to count negative values
	//
	int count = 0;
	vector<long>::iterator p;
	p = find_if(v.begin(), v.end(), isMinus);
	while(p != v.end()) {
		count ++;
		p = find_if(p+1, v.end(), isMinus);
	}
	cout << "Number of values: " << VSIZE << endl;
	cout << "negative values : " << count << endl;

	return 0 ;
}

// Set ri to a signed integer value
void initialize(long &ri)
{
	ri = (random() - (RAND_MAX / 2) );
	// ri = random();
}

// Display value of ri
void show(const long &ri)
{
	cout << ri << " ";
}

// Returns true if ri is less than 0
bool isMinus(const long &ri)
{
	return (ri<0);
}