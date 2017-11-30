#include <stack>
#include <iostream>
#include <ostream>
using namespace std;

ostream & operator<<(ostream & os, stack<double> my_stack) //function header
{
    while(!my_stack.empty()) //body
    {
        os << my_stack.top() << " ";
        my_stack.pop();
    }
    return os; // end of function
}

int main(){
stack<int> mystack;


mystack.push(1);
mystack.push(3);

cout<<mystack<<endl;

return 0; 
}

