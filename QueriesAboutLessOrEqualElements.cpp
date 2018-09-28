#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  //Read the size of vectors
  int n, m;
  cin >> n;
  cin >> m;

  //Read elements of vectors
  vector<int> a(n);
  vector<int> b(m);
  for(int i = 0; i < n; i++) {
    cin >> a[i];
  }

  for(int j = 0; j < m; j++) {
    cin >> b[j];
  }

  //Sort array a
  sort(a.begin(), a.end());

  //Try every element in B
  vector <int>::iterator up;
  for(int k = 0; k < b.size(); k++) {
    cout << (upper_bound(a.begin(), a.end(), b[k]))-a.begin() << " ";
  }
  cout << "\n";

  return 0;
}
