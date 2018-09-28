#include <stdio.h>

int main() {

  //Read the nunber of cases
  int cases;
  scanf("%d", &cases);

  //Read the cases
  int pos[1000][2];
  int n;
  for(int i = 0; i < cases; i++) {
    //Read the number of people
    scanf("%d", &n);

    //Read the position
    for(int j = 0; j < n; j++) {
      scanf("%d %d", &pos[j][0], &pos[j][1]);
    }
  }

  

  return 0;
}
