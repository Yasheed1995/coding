
#ifndef _GANN_H_
#define _GANN_H_

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>

using namespace std;

#define SIZE 10

#define WINDOW 15
#define G 100000
#define X_GRID 78
#define Y_GRID 23


inline double rand(double a, double b) {
	return ((double)rand()/(double)RAND_MAX * (b-a)) +a;
}

inline double randNormal(double mean, double stdev) {
	double y1 = rand(0,1);
	double y2 = rand(0,1);
	while (y1 < DBL_MIN) y1 = rand(0,1);
	return mean + stdev * sqrt(-2*log(y1)) 
	* cos(2*3.1415926535897*y2);

}

class GANN {
public:
	GANN() {
		srand(unsigned long)time(NULL);
		generation = 0;
		stepSize = 0.01;

		parent = new double[SIZE];
		offspring = new double[SIZE];
		record = new int[WINDOW];

		for (int i=0; i<SIZE; i++)
			parent[i] = 0.0;
		parentFitness = evaluate(parent);

		for (int i=0; i<WINDOW; i++) {
			if ((i%5 == 0)) record[i] = 1;
			else record[i] = 0;
		}
		recordIndex = 0;
	}

	~GANN() {
		delete [] parent;
		delete [] offspring;
		delete [] record;
	}

	void trainOnce() {

		for (int i=0; i<SIZE; i++){
			double x = randNormal(0,stepSize);
			if (x<-0.1) x=-0.1;
			if (x>0.1) x=0.1;
			offspring[i] = parent[i] + x;
		}

		double offspringFitness = evaluate(offspring);

		if (offspringFitness < parentFitness) {
			for (int i=0; i<SIZE; i++)
				parent[i] = offspring[i];
			parentFitness = offspringFitness;

			record[recordIndex] = 1;
			recordIndex = (recordIndex + 1) % WINDOW;
		}
		else {
			record[recordIndex] = 0;
			recordIndex = (recordIndex + 1) % WINDOW;
		}

		int count = 0;
		for (int i=0; i< WINDOW; i++)
			if (record[i] == 1) count++;

		if (count * 5) > WINDOW)	
			stepSize /= pow(0.817, 1.0/SIZE);
		else if (count * 5 < WINDOW)
			stepSize *= pow(0.817, 1.0/SIZE);

		generation ++;

		if (generation % 1000 == 0)
			cout << fixed << setprecision(6) << "Generation "
		<< generation << ": (" 
		<< (double) parentFitness/X_GRID/Y_GRID
		<< "," << stepSize << ")" << endl;
		}
};

















