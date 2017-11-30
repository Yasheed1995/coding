#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <fstream>
using std::fstream;
using std::ios;

typedef unsigned char   BYTE;
typedef unsigned short  WORD;
typedef unsigned long   DWORD;
typedef long            LONG;

int main(){
    fstream file;
        int i,j;
    char fileName[32], RGBQUAD[4][256], PIXEL[128][128],temp[128][128];
    

    WORD bfType;
    DWORD bfSize;
    WORD bfReserved1;
    WORD bfReserved2;
    DWORD bfOffBits;
    DWORD biSize;
    LONG biWidth;
    LONG biHeight;
    WORD biPlanes;
    WORD biBitCount;
    DWORD biCompression;
    DWORD biSizeImage;
    LONG biXPelsPerMeter;
    LONG biYPelsPerMeter;
    DWORD biClrUsed;
    DWORD biClrImportant;

    //將資料從檔案輸入到記憶體
        cout << "Open FileName: ";
    cin >> fileName;

    file.open(fileName, ios::in|ios::binary);
    file.read((char*)&bfType, sizeof(WORD));
    file.read((char*)&bfSize, sizeof(DWORD));
    file.read((char*)&bfReserved1, sizeof(WORD));
    file.read((char*)&bfReserved2, sizeof(WORD));
    file.read((char*)&bfOffBits, sizeof(DWORD));
    file.read((char*)&biSize, sizeof(DWORD));
    file.read((char*)&biWidth, sizeof(LONG));
    file.read((char*)&biHeight, sizeof(LONG));
    file.read((char*)&biPlanes, sizeof(WORD));
    file.read((char*)&biBitCount, sizeof(WORD));
    file.read((char*)&biCompression, sizeof(DWORD));
    file.read((char*)&biSizeImage, sizeof(DWORD));
    file.read((char*)&biXPelsPerMeter, sizeof(LONG));
    file.read((char*)&biYPelsPerMeter, sizeof(LONG));
    file.read((char*)&biClrUsed, sizeof(DWORD));
    file.read((char*)&biClrImportant, sizeof(DWORD));
    file.read(RGBQUAD[0], sizeof(RGBQUAD));
    file.read(PIXEL[0], sizeof(PIXEL));
    file.close();

    //顯示檔案資訊
        cout << "FILE_HEADER\n"
         << "bfType=\t\t"       << bfType       << '\n'
         << "bfSize=\t\t"       << bfSize       << '\n'
         << "bfReserved1=\t"    << bfReserved1  << '\n'
         << "bfReserved2=\t"    << bfReserved2  << '\n'
         << "bfOffBits=\t"      << bfOffBits    << "\n\n"
         << "INFO_HEADER\n"
         << "biSize=\t\t"       << biSize       << '\n'
         << "biWidth=\t"        << biWidth      << '\n'
         << "biHeight=\t"       << biHeight     << '\n'
         << "biPlanes=\t"       << biPlanes     << '\n'
         << "biBitCount=\t"     << biBitCount   << '\n'
         << "biCompression=\t"  << biCompression    << '\n'
         << "biSizeImage=\t"    << biSizeImage      << '\n'
         << "biXPelsPerMeter="  << biXPelsPerMeter  << '\n'
         << "biYPelsPerMeter="  << biYPelsPerMeter  << '\n'
         << "biClrUsed=\t"      << biClrUsed        << '\n'
         << "biClrImportant=\t" << biClrImportant   << "\n\n";

                //將圖片資訊暫存到TEMP裡面
                for(i=127;i>=0;i--){
                        for(j=127;j>=0;j--){
                                temp[i][j]=PIXEL[i][j];
                                }
                        }
                        //將資訊反轉180度
                for(i=0;i<=127;i++){
                        for(j=0;j<=127;j++){
                                PIXEL[127-i][127-j]=temp[i][j];
                                }
                        }
                //將資料從記憶體輸出到檔案        
                cout << "輸入旋轉後儲存的名稱：\t";
            cin >> fileName;

                file.open(fileName, ios::out|ios::binary);
                file.write((char*)&bfType, sizeof(WORD));
                file.write((char*)&bfSize, sizeof(DWORD));
                file.write((char*)&bfReserved1, sizeof(WORD));
                file.write((char*)&bfReserved2, sizeof(WORD));
                file.write((char*)&bfOffBits, sizeof(DWORD));
                file.write((char*)&biSize, sizeof(DWORD));
                file.write((char*)&biWidth, sizeof(LONG));
                file.write((char*)&biHeight, sizeof(LONG));
                file.write((char*)&biPlanes, sizeof(WORD));
                file.write((char*)&biBitCount, sizeof(WORD));
                file.write((char*)&biCompression, sizeof(DWORD));
                file.write((char*)&biSizeImage, sizeof(DWORD));
                file.write((char*)&biXPelsPerMeter, sizeof(LONG));
                file.write((char*)&biYPelsPerMeter, sizeof(LONG));
                file.write((char*)&biClrUsed, sizeof(DWORD));
                file.write((char*)&biClrImportant, sizeof(DWORD));
                file.write(RGBQUAD[0], sizeof(RGBQUAD));
                file.write(PIXEL[0], sizeof(PIXEL));
                file.close();
}



