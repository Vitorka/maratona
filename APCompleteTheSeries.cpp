#include <iostream>
#include <string>
using namespace std;

int main() {

  //Read the number of test cases
  int cases;
  cin >> cases;

  //Variables for the 3rd element, 3rd last element and sum
  long long int telement, tlelement, s;

  //n, p, and first element of PA
  long long int n, p, felement;

  for(int i = 0; i < cases; i++) {
    cin >> telement;
    cin >> tlelement;
    cin >> s;

    //Calculate n
    n = (2*s)/(telement + tlelement);

    //Calculate p
    p = (tlelement - telement) / (n - 5);

    //Calculate first element
    felement = telement - 2*p;

    cout << n << "\n";

    for(int j = 0; j < n; j++) {
      cout << felement + (p * j) << " ";
    }

    cout << "\n";
  }

  return 0;
}
