#include <iostream>

using namespace std;

// template <typename T>
// T func(T z) {
//     return z * z;
// }

auto func = [](auto i){ return i * i; };

int main(){
    auto result = [](int input){ return input * input; };
    cout << result(12) << endl;
    cout << result(13) << endl;
    cout << result(15) << endl;
    cout << func(19) << endl;
    return 0;
}
    
