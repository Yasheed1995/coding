/****************************************************************************
  FileName     [ cirMgr.cpp ]
  PackageName  [ cir ]
  Synopsis     [ Define cir manager functions ]
  Author       [ Chung-Yang (Ric) Huang ]
  Copyright    [ Copyleft(c) 2008-present LaDs(III), GIEE, NTU, Taiwan ]
****************************************************************************/

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <ctype.h>
#include <cassert>
#include <cstring>
#include "cirMgr.h"
#include "cirGate.h"
#include "util.h"
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

// TODO: Implement memeber functions for class CirMgr

/*******************************/
/*   Global variable and enum  */
/*******************************/
CirMgr* cirMgr = 0;

enum CirParseError {
   EXTRA_SPACE,
   MISSING_SPACE,
   ILLEGAL_WSPACE,
   ILLEGAL_NUM,
   ILLEGAL_IDENTIFIER,
   ILLEGAL_SYMBOL_TYPE,
   ILLEGAL_SYMBOL_NAME,
   MISSING_NUM,
   MISSING_IDENTIFIER,
   MISSING_NEWLINE,
   MISSING_DEF,
   CANNOT_INVERTED,
   MAX_LIT_ID,
   REDEF_GATE,
   REDEF_SYMBOLIC_NAME,
   REDEF_CONST,
   NUM_TOO_SMALL,
   NUM_TOO_BIG,

   DUMMY_END
};

/**************************************/
/*   Static varaibles and functions   */
/**************************************/
static unsigned lineNo = 0;  // in printint, lineNo needs to ++
static unsigned colNo  = 0;  // in printing, colNo needs to ++
static char buf[1024];
static string errMsg;
static int errInt;
static CirGate *errGate;

static bool
parseError(CirParseError err)
{
   switch (err) {
      case EXTRA_SPACE:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Extra space character is detected!!" << endl;
         break;
      case MISSING_SPACE:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Missing space character!!" << endl;
         break;
      case ILLEGAL_WSPACE: // for non-space white space character
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Illegal white space char(" << errInt
              << ") is detected!!" << endl;
         break;
      case ILLEGAL_NUM:
         cerr << "[ERROR] Line " << lineNo+1 << ": Illegal "
              << errMsg << "!!" << endl;
         break;
      case ILLEGAL_IDENTIFIER:
         cerr << "[ERROR] Line " << lineNo+1 << ": Illegal identifier \""
              << errMsg << "\"!!" << endl;
         break;
      case ILLEGAL_SYMBOL_TYPE:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Illegal symbol type (" << errMsg << ")!!" << endl;
         break;
      case ILLEGAL_SYMBOL_NAME:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Symbolic name contains un-printable char(" << errInt
              << ")!!" << endl;
         break;
      case MISSING_NUM:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Missing " << errMsg << "!!" << endl;
         break;
      case MISSING_IDENTIFIER:
         cerr << "[ERROR] Line " << lineNo+1 << ": Missing \""
              << errMsg << "\"!!" << endl;
         break;
      case MISSING_NEWLINE:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": A new line is expected here!!" << endl;
         break;
      case MISSING_DEF:
         cerr << "[ERROR] Line " << lineNo+1 << ": Missing " << errMsg
              << " definition!!" << endl;
         break;
      case CANNOT_INVERTED:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": " << errMsg << " " << errInt << "(" << errInt/2
              << ") cannot be inverted!!" << endl;
         break;
      case MAX_LIT_ID:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Literal \"" << errInt << "\" exceeds maximum valid ID!!"
              << endl;
         break;
      case REDEF_GATE:
         cerr << "[ERROR] Line " << lineNo+1 << ": Literal \"" << errInt
              << "\" is redefined, previously defined as "
              << errGate->getTypeStr() << " in line " << errGate->getLineNo()
              << "!!" << endl;
         break;
      case REDEF_SYMBOLIC_NAME:
         cerr << "[ERROR] Line " << lineNo+1 << ": Symbolic name for \""
              << errMsg << errInt << "\" is redefined!!" << endl;
         break;
      case REDEF_CONST:
         cerr << "[ERROR] Line " << lineNo+1 << ", Col " << colNo+1
              << ": Cannot redefine constant (" << errInt << ")!!" << endl;
         break;
      case NUM_TOO_SMALL:
         cerr << "[ERROR] Line " << lineNo+1 << ": " << errMsg
              << " is too small (" << errInt << ")!!" << endl;
         break;
      case NUM_TOO_BIG:
         cerr << "[ERROR] Line " << lineNo+1 << ": " << errMsg
              << " is too big (" << errInt << ")!!" << endl;
         break;
      default: break;
   }
   return false;
}

/**************************************************************/
/*   class CirMgr member functions for circuit construction   */
/**************************************************************/
bool
CirMgr::readCircuit(const string& fileName)
{
    CirGate* ccGate;
    ifstream ifs(fileName); // read file
    string line = "";
    // read the first header line
    getline(ifs, line);
    stringstream ss(line);
    vector<int> header;
    string n;
    int nn;
    while(getline(ss, n, ' ')) {
        if(!myStr2Int(n, nn)) continue;
        header.push_back(nn);
    } 

#define M header[0]
#define I header[1]
#define L header[2]
#define O header[3]
#define A header[4]    
cout << M << endl;
cout << I << endl;
cout << L << endl;
cout << O << endl;
cout << A << endl;
    // contruct all gates
    while(getline(ifs, line)){
        stringstream strstr(line);
        string first_word;
        int GateNum;
        getline(strstr, first_word, ' ');
        if(!myStr2Int(first_word, GateNum)) break; // if the first num is not int 
        ccGate = new AigGate(GateNum/2);    // new gates(unknown type!!)
        _GateMap.insert(pair<unsigned, AigGate*>(GateNum, ccGate)); // insert to map
    }
    // read again
    ifs.clear();
    ifs.seekg(0, ifs.beg);
    // read pi po and connect
    
    int count = 0;
    int count_alias = 0;
    while(getline(ifs, line)) {
        if(line == "c") { cout << "stopped c" << endl;}
        if(count > 0 && count <= I){
            _PiList.push_back(stoi(line));
        }
        else if(count <= (I + O)){
            _PoList.push_back(stoi(line));
        }
        else if(count <= (I + O + L)){

        }
        else if(count <= (I + O + L + A)){
            stringstream strstr2(line);
            string word;
            int gNum;
            vector<int> gNums;

            while(getline(strstr2, word, ' ')){
                if(!myStr2Int(word, gNum)) break;
                gNums.push_back(gNum);
            }
            IOGate *io1_in, *in2_in;
            connect(gNums[0], gNums[1], gNums[2]);
        } 

        else{
            stringstream strstr3(line);
            string symbol_alias;
            vector<string> symbols;

            while(getline(strstr3, symbol_alias, ' ')){
                symbols.push_back(symbol_alias);
            } 
            symbol_alias = symbols[1];
            if(count_alias <= I){
                _GateMap[_PiList[count_alias]]->set_symbol(symbol_alias);
            }

            ++ count_alias;
        }


    
        ++ count;
    }   
    return true;
}

/**********************************************************/
/*   class CirMgr member functions for circuit printing   */
/**********************************************************/
/*********************
Circuit Statistics
==================
  PI          20
  PO          12
  AIG        130
------------------
  Total      162
*********************/
void
CirMgr::printSummary() const
{
}

void
CirMgr::printNetlist() const
{
}

void
CirMgr::printPIs() const
{
   cout << "PIs of the circuit:";
   cout << endl;
}

void
CirMgr::printPOs() const
{
   cout << "POs of the circuit:";
   cout << endl;
}

void
CirMgr::printFloatGates() const
{
}

void
CirMgr::writeAag(ostream& outfile) const
{
}
