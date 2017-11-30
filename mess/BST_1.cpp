#include <iostream>

using namespace std;

class Node {
public:
	Node() { left = right = NULL;}
	Node(int val) {
		left = right = NULL;
		data = val;
	}
	Node *left;
	Node *right;
	int data;
};

class BST {
public:
	BST() { root = NULL; }

	void insert(int val) {
		if (root == NULL) {
			root = new Node(val);
		}
		else
			insert(root, val);
	}

	~BST() {
		if( root != NULL)
			release(root);
	}

	bool search(int val) const {
		if(root == NULL)
			return false;
		return search(root, val);
	}

	void inorder() const {
		if (root != NULL)
			inorder(root);
		cout << endl;
	}

	void preorder() const {
		if(root != NULL)
			preorder(root);
		cout<<endl;
	}
	void postorder() const {
		if(root != NULL)
			postorder(root);
		cout<<endl;
	}

protected:

	void release(Node* p) {
		if (p->left != NULL)
			release(p->left);
		if (p->right != NULL)
			release(p->right);
		cout << "releasing " << p->data << "..." <<endl;                           
		delete p;
	}

	void inorder(Node* p) const {
		if (p->left != NULL)
			inorder(p->left);
		cout << p->data << ' ';
		if (p->right != NULL)
			inorder(p->right);
	}

	void preorder(Node* p) const {
		cout << p->data << ' ';
		if (p->left != NULL)
			preorder(p->left);
		if (p->right != NULL)
			preorder(p->right);
	}

	void postorder(Node* p) const {
		if (p->left != NULL)
			preorder(p->left);
		if (p->right != NULL)
			preorder(p->right);
		cout << p->data << ' ';
	}

	// p cannot be NULL
	void insert(Node* p, int val) {

		if (p->data > val)  {
			// left 
			if( p->left == NULL)
				p->left = new Node(val);
			else
				insert(p->left, val);
		}
		else{
			// right
			if (p->right == NULL)
				p->right = new Node(val);
			else 
				insert(p->right, val);
		}
	}

	// p cannot be NULL
	bool search(Node* p, int val) const {
		if (p->data == val)
			return true;
		if (p->data > val) {
			// left
			if ( p-> left == NULL)
				return false;
			return search(p->left, val);
		}
		else {
			// right 
			if (p->right == NULL)
				return false;
			return search(p->right,val);
		}
	}

protected:
	Node* root;
};

int main()
{
	BST bst;
	bst.insert(3);
	bst.insert(6);
	bst.insert(4);
	bst.insert(7);
	bst.insert(2);
	bst.insert(0);
	bst.insert(1);
	bst.insert(9);

	cout << bst.search(13) << endl;
	cout << bst.search(7) << endl;
	bst.inorder();
	bst.preorder();
	bst.postorder();
	return 0;
}
























