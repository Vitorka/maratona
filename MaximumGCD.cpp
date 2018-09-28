#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int gcd(int a, int b) {
  if(a % b == 0) {
    return b;
  } else {
    return gcd(b, a % b);
  }
}

int main() {

  string number;

  getline(cin, number);

  int n = stoi(number);

  for(int k = 0; k < n; k++) {
    string str, token;

    getline(cin, str);

    vector <string> teste;

    stringstream ss(str);

    while(getline(ss, token, ' ')) {
      teste.push_back(token);
    }

    int resultado = 0, aux;

    for(int i = 0; i < teste.size(); i++) {
      for(int j = i + 1; j < teste.size(); j++) {
        aux = gcd(stoi(teste[i]), stoi(teste[j]));

        if(aux > resultado) {
          resultado = aux;
        }
      }
    }

    cout << resultado << "\n";
  }


  return 0;
}
