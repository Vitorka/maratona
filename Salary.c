#include <stdio.h>
#include <string.h>

int main() {

  //Read the salary
  char salary[2002];
  scanf("%s", salary);

  //Verify the salary in case that the salary given is not a palindrome

  int i, j, left, right;

  //Verify if the salary has a even or odd number of characters
  if(!(strlen(salary) % 2)) { //even
    left = (strlen(salary) / 2) - 1;
    right = strlen(salary) / 2;
  } else { //odd
    left = right = strlen(salary) / 2;
  }

  i = left;
  j = right;

  //Change characters to obtain palindromes
  while((i >= 0) && (j <= strlen(salary))) {

    int dif_left, dif_right;

    if(salary[i] != salary[j]) {
      dif_left = i;
      dif_right = j;

      char sal_dif_right, sal_dif_left;
      sal_dif_left = salary[i];
      sal_dif_right = salary[j];

      //Copy left side to right side
      while((i >= 0) && (j <= strlen(salary))) {
        salary[j] = salary[i];
        i--;
        j++;
      }

      //Verify if the middle numbers have to be fixed
      if(sal_dif_right > sal_dif_left) {

        if((salary[left] == '9') && (salary[right] == '9')) {
          salary[left] = '0';
          salary[right] = '0';
          left--;
          right++;

          while((left > dif_left) && (right < dif_right)) {
            if((salary[left] == '9') && (salary[right] == '9')) {
              salary[left] = '0';
              salary[right] = '0';
            } else if((salary[left] != '9') && (salary[right] != '9')) {
              salary[left] += 1;
              salary[right] += 1;
              break;
            }
            left--;
            right++;
          }

          if((salary[dif_left + 1] == '0') && (salary[dif_right - 1] == '0')) {
            salary[dif_left] += 1;
            salary[dif_right] += 1;
          }

        } else {
          if(!(strlen(salary) % 2)) { //even
            salary[left] += 1;
            salary[right] += 1;
          } else { //odd
            salary[left] += 1;
          }
        }
      }
    }

    i--;
    j++;
  }


  printf("%s\n", salary);

  return 0;
}
