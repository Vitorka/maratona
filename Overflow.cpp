#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {

  char n1[50000], n2[50000], op;
  long double x, y, result;
  int max = 2147483647;

  while(scanf("%s %c %s", n1, &op, n2) == 3) {
    x = atof(n1);
    y = atof(n2);

    cout << n1 << ' ' << op << ' ' << n2 << '\n';

    if(op == '+') {
      result = x + y;
    } else if(op == '*') {
      result = x * y;
    }

    if(x >= max) {
      cout << "first number too big\n";
    }
    if (y >= max) {
      cout << "second number too big\n";
    }
    if(result >= max) {
      cout << "result too big\n";
    }
  }

  return 0;
}
