#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {

  //Le o numero de linhas
  int n;
  cin >> n;

  for(int i = 0; i < n; i++) {
    int x, y;
    int a, b;

    cin >> x;
    cin >> y;

    a = (x + y)/2;
    b = (x - y)/2;

    if((a < 0) || (b < 0) || ((x + y) % 2 != 0) || ((x - y) % 2 != 0)) {
      cout << "impossible\n";
    } else {
      cout << a << ' ' << b << '\n';
    }

  }
  return 0;
}
