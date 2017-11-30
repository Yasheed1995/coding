#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// function that prints the passed argument
void print (int elem)
{
    cout << elem << ' ';
}
void printV(vector<int> vec){
    for_each (vec.begin(), vec.end(),    // range
              print);   
}

int main(void)
{

    vector<int> v1(4,400);
    cout << "v1: " ;
    printV(v1);
    cout << endl;
    vector<int> v2(v1.begin(), v1.end());
    cout << "v2: " ;
    printV(v2);
    cout << endl;
    int arr[] = {1,2,3,4,5};
    vector<int> v3(arr,arr + sizeof(arr)/sizeof(int));
    printV(v3);
    cout << endl;
}
