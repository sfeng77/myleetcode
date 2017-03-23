#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        while (n%2 ==0) n=n/2;
        while (n%3 ==0) n=n/3;
        while (n%5 ==0) n=n/5;
        return (n==1);
    }  
};


Int main(){
  Solution s;
  cout << s.isUgly(-2147483648) << '\n';
  return 0;
}
