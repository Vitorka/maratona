#include <iostream>
#include <string>
using namespace std;

int main() {

  //Number of cases
  int cases;
  cin >> cases;

  //Coordinates
  long long int x, y;

  for(int i = 0; i < cases; i++) {

    //Read Coordinates
    cin >> x;
    cin >> y;

    if((x == y) || (x - y == 2)) {
        if(x % 2 == 0) {
          cout << x + y << "\n";
        } else {
          cout << x + y - 1 << "\n";
        }
    } else {
      cout << "No Number\n";
    }
  }

  return 0;
}
