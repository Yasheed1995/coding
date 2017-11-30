#include <iostream>
#include <string>

using namespace std;

class Base {

public:
	virtual void print() const = 0;

};

class MyInt: public Base {
public:
	MyInt(int _n): n(_n) { }

protected:
	int n;
	void print() const {
		cout << n << endl;
	}
};

class MyString: public Base {
public: 
	MyString(string _s): s(_s) { }

protected:
	string s;
	void print() const {
		cout << "\"" << s << "\"" << endl;
	}
};

int main()
{
	int choice;
	cin >> choice;
	Base *p;

	if (choice == 1)
		p = new MyInt(5);
	else
		p = new MyString("Hello");

	p->print();

	return 0;
}










