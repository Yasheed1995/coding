#include <iostream>
#include <algorithm>

using namespace std;

#define SIZE 100
int iarray[SIZE];

int main(){
	iarray[20] = 50;
	iarray[50] = 50;
	int *IP = find(iarray,iarray+SIZE,50);
	while(!(IP == iarray + SIZE)){
		int *IP = find(iarray,iarray+SIZE,50);
		if(IP == iarray + SIZE)
			cout << "not find" << endl;
		else
			cout << *IP << " found" << endl;
			IP++;
	}
	return 0;
}