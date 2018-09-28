#include <stdio.h>
#include <math.h>

int main() {

  unsigned long int n;
  unsigned long int p[2][2];
  unsigned long int final_p = 0, final_a;

  //Read the number N
  scanf("%lu", &n);

  p[0][0] = 1;
  p[0][1] = (-(2*1 - 1) + sqrt((double)((2*1 - 1) * (2*1 - 1) + 8*n)))/2*1;
  p[1][0] = 1;
  p[1][1] = (-(2*1 - 1) - sqrt((double)((2*1 - 1) * (2*1 - 1) + 8*n)))/2*1;
  printf("p1 = %lu\np2 = %lu\n\n", p[0][1], p[1][1]);

  for(int a = 1; a <= n; a++) {

    if(p[0][0] > final_p) {
      final_a = p[0][0];
      final_p = p[0][1];
    }
    if(p[1][0] > final_p) {
      final_a = p[1][0];
      final_p = p[1][1];
    }

    p[0][0] = a;
    p[0][1] = (-(2*a - 1) + sqrt((double)(((2*a - 1) * (2*a - 1)) + 8*n)))/2*a;
    p[1][0] = a;
    p[1][1] = (-(2*a - 1) - sqrt((double)((2*a - 1) * (2*a - 1) + 8*n)))/2*a;

    printf("p1 = %lu\np2 = %lu\n\n", p[0][1], p[1][1]);

  }

  printf("A = %lu\nP = %lu\n", final_a, final_p);

  return 0;
}
