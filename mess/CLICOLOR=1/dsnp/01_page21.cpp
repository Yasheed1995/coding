// pointers

#include <iostream>
using namespace std;



int main()
{
    int i = 10;
    int* p = new int(100);
    int j = i;
    int* q = p;
    cout << "The address of i is: " << &i << endl;
    cout << "The address of p is: " << &p << endl;
    cout << "The address of j is: " << &j << endl;
    cout << "The address of q is: " << &q << endl;
    cout << "The content of i is: " << i << endl;
    cout << "The content of p is: " << p << endl;






}
