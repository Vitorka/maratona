#include <stdio.h>

int main() {

  //Read the N hieroglyphs
  int n;
  scanf("%d", &n);

  //Read hieroglyphs
  char hie[n][3];
  for(int i = 0; i < n; i++) {
    scanf("%s", hie[i]);
  }
  scanf(" ");
  //Read the letter given
  char letter;
  scanf("%c", &letter);

  //Find hieroglyphs with the letter
  for(int i = 0; i < n; i++) {
    if(hie[i][0] == letter) {
      printf("%s\n", hie[i]);
    }
  }

  return 0;
}
