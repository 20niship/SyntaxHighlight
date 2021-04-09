#include <iostream>
using namespace std;
#define TEST__ 123

enum class hoge{
  enum_1 : 1,
  enum_2 : 2,
  enum_3 : 3
};


struct huga{
std::vector<std::vector<int>> vec1;
std::string str1;

  int test(){
    printf("Hello, World!!"); // This is comment
    /*  
    Comment 1
    Comment 2
    Comment 3
    */
  return 0;
  }
}


int main(){
  cout << "Hello world." << endl;
  return 0;
}