/****************************************************************************
  FileName     [ cirGate.h ]
  PackageName  [ cir ]
  Synopsis     [ Define basic gate data structures ]
  Author       [ Chung-Yang (Ric) Huang ]
  Copyright    [ Copyleft(c) 2008-present LaDs(III), GIEE, NTU, Taiwan ]
****************************************************************************/

#ifndef CIR_GATE_H
#define CIR_GATE_H

#include <string>
#include <vector>
#include <iostream>
#include "cirDef.h"
#include "cirGate.h"

using namespace std;

class CirGate;
class AigGate;
class IOGate;
//------------------------------------------------------------------------
//   Define classes
//------------------------------------------------------------------------
// TODO: Define your own data members and member functions, or classes
class CirGate
{
public:
   CirGate(size_t num = 0) : _ID(num) {}
   virtual ~CirGate() {}

   // Basic access methods
   string getTypeStr() const { return ""; }
   unsigned getLineNo() const { return 0; }

   // Printing functions
   virtual void printGate() const = 0;
   void reportGate() const;
   void reportFanin(int level) const;
   void reportFanout(int level) const;

   void set_symbol(string symbol){
        _symbol = symbol;
   }

   void push_fanin(IOGate* x);
       
   void push_fanout(IOGate* x);
        
private:

protected:
    vector<IOGate*> _faninList;
    vector<IOGate*> _fanoutList;
    static size_t _globalRef_s;
    size_t _ref;
    size_t _ID;
    string _symbol;
};

class AigGate : public CirGate
{
public:
    AigGate(size_t x) : CirGate(x) {}
    ~AigGate() {}
    void printGate() const {}    

private:
};

class IOGate 
{
    friend class CirGate;
    #define NEG 0x1
public:
    IOGate(AigGate* g, size_t phase = 0):
        _gateV(size_t(g) + phase) {}
    AigGate* gate() const {
        return (AigGate*)(_gateV & ~size_t(NEG)); }
    bool isInv() const {
        return (_gateV & NEG); }
private:
    size_t _gateV;
};

#endif // CIR_GATE_H
