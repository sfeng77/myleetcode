#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
      int *notPrime = new int[n]();

      int i,j,count;
      int sqrN = sqrt(n);

      for (i=2;i<=sqrN;i++){
	for(j=i+i;j<n;j+=i)
	  notPrime[j] = 1;
      }

      count = 0;
      for(i=2;i<n;i++)
	count += 1- notPrime[i];
      
      delete [] notPrime;
      return count;
    }
  
};


int main(){
  Solution s;
  cout << s.countPrimes(10) << '\n';
  
  return 0;
}
