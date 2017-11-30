#include <iostream>
using namespace std;

class Rectangle {
	int width, height;
public:
	Rectangle();
	Rectangle(int, int);
	int area() {return (width * height);}

};

Rectangle::Rectangle(){
	width = 5;
	height = 5;
}

Rectangle::Rectangle(int a, int b){
	width = a;
	height = b;
}

int main(){
	Rectangle rect1(3,4);
	Rectangle rect2;
	cout << "rect1 area: " << rect1.area() << endl;
	cout << "rect2 area: " << rect2.area() << endl;
	return 0;
}