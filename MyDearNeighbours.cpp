#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
  vector <int> neighbours;

  //Read the number of test cases
  string number;
  getline(cin, number);
  int n = stoi(number);

  //Test the test cases
  for(int i = 0; i < n; i++) {

    //Read the number of places that Manuel can live
    string nplaces;
    getline(cin, nplaces);
    int p = stoi(nplaces);

    //Read the number of neighbours for each place
    string place, token;
    stringstream stream;
    for(int j = 0; j < p; j++) {
      getline(cin, place);
      //cout << place << "\n";
      stringstream stream(place);
      int count = 0;

      while(getline(stream, token, ' ')) {
        count++;
      }
      neighbours.push_back(count);
    }

    //cout << min_element(neighbours.begin(), neighbours.end()) - neighbours.begin() << "\n";
    vector <int>::iterator it = min_element(neighbours.begin(), neighbours.end());
    neighbours.erase (it);

    for(int i = 0; i < neighbours.size(); i++) {
      cout << neighbours[i] << "\n";
    }
  }

  return 0;
}
