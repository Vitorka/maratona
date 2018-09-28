#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {
  string n, p;
  getline(cin, n);
  getline(cin, p);

  int i, j;
  i = stoi(n);
  j = stoi(p);

  for(int k = 0; k < j; k++) {
    cout << k << "\n";
  }

  string str, token;

  getline(cin, str);

  vector <string> teste;

  stringstream ss(str);

  while(getline(ss, token, ' ')) {
    teste.push_back(token);
  }

  for(int i = 0; i < teste.size(); i++) {
    //cout << teste[i] << "\n";
  }

  return 0;
}
