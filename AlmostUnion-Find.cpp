#include <bits/stdc++.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {

  vector <string> teste;

  string str, token;

  getline(cin, str);

  stringstream ss(str);

  while(getline(ss, token, ' ')) {
    teste.push_back(token);
  }

  int n = stoi(teste[0]);
  int m = stoi(teste[1]);

  for(int i = 0; i < m; i++) {

    getline(cin, str);

    stringstream ss(str);

    while(getline(ss, token, ' ')) {
      teste.push_back(token);
    }

  }

  cout << teste[0] << ' ' << teste[1] << "\n";

  return 0;
}
