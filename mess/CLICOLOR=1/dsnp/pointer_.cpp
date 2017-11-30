#include <iostream>
using namespace std;

bool moveBufPtr(char* const ptr){
  if(ptr > readBufEnd || ptr < readBufPtr){
      mybeep();
      return false;
  }
  else
      readBufptr = ptr;
}

int main()
{
  char _readBuf[65536];
  char* readBufPtr;
  char* readBufEnd;
  
  _readBuf[0] = 1;
  _readBuf[1] = 3;
  

}
