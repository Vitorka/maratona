#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

unsigned long long int fibonacci(unsigned long long int n) {
  unsigned long long int a = 0, b = 1, aux;

  if(n == 0) {
    return 0;
  } else if(n == 1) {
    return 1;
  }

  for(unsigned long long int i = 1; i < n; i++) {
    aux = a + b;
    a = b;
    b = aux;
  }
  return b;
}

int main() {

  unsigned long long int n, m, r, i, c, j;

  cin >> c;

  for(j = 0; j < c; j++) {
    r = 0;
    cin >> n;
    cin >> m;

    for(i = n; i <= m; i++) {
      r += (fibonacci(i) % 1000000007);
    }

    cout << r << "\n";
  }

  return 0;
}
