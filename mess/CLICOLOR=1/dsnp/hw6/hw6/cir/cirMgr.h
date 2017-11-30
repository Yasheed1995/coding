/****************************************************************************
  FileName     [ cirMgr.h ]
  PackageName  [ cir ]
  Synopsis     [ Define circuit manager ]
  Author       [ Chung-Yang (Ric) Huang ]
  Copyright    [ Copyleft(c) 2008-present LaDs(III), GIEE, NTU, Taiwan ]
****************************************************************************/

#ifndef CIR_MGR_H
#define CIR_MGR_H

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <map>
#include <stack>

using namespace std;

#include "cirDef.h"
#include "cirGate.h"
extern CirMgr *cirMgr;
class IOGate;

class AigGate;
// TODO: Define your own data members and member functions

//extern IOGate* io1_out, *io2_out, *io1_in, *io2_in;
//extern AigGate* aigO, *aigI1, *aigI2;
class CirMgr
{
public:
   CirMgr(){}
   ~CirMgr() {}

   // Access functions
   // return '0' if "gid" corresponds to an undefined gate.
   CirGate* getGate(unsigned gid) const { return 0; }

   // Member functions about circuit construction
   bool readCircuit(const string&);

   // Member functions about circuit reporting
   void printSummary() const;
   void printNetlist() const;
   void printPIs() const;
   void printPOs() const;
   void printFloatGates() const;
   void writeAag(ostream&) const;


   void connect(unsigned FanOutGate, unsigned FanIn_1, unsigned FanIn_2);
   

private:
   map<size_t, AigGate*> _GateMap;
   IdList _PiList;
   IdList _PoList; 
   GateList _TotalList;

};

void CirMgr::connect(unsigned FanOutGate, unsigned FanIn_1, unsigned FanIn_2)
   {
        // io1_out, io2_out: for FanOutGate 
        IOGate* io1_out, *io2_out, *io1_in, *io2_in;
        AigGate* aigO, *aigI1, *aigI2;
        size_t phase1, phase2;
        phase1 = (FanIn_1 % 2 == 1) ? 1 : 0;
        phase2 = (FanIn_2 % 2 == 1) ? 1 : 0;
        aigI1 = _GateMap[FanIn_1/2];
        aigI2 = _GateMap[FanIn_2/2];
        aigO = _GateMap[FanOutGate/2];
        io1_out = new IOGate(aigI1, phase1);
        io2_out = new IOGate(aigI2, phase2);
        io1_in = new IOGate(aigO);
        io2_in = io1_in;
        aigO->push_fanin(io1_out);
        aigO->push_fanin(io2_out);
        aigI1->push_fanout(io1_in);
        aigI2->push_fanout(io2_in);
   }

#endif // CIR_MGR_H

