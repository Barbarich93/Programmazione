#include <stdio.h>

int main(){
    int n = 10;
    int fattoriale = 1;
    while (n > 0){
        fattoriale=fattoriale*n;
        n--;
    }
printf("\nFattoriale = %d",fattoriale);
char c = 'a';
while (c != 'v'){
    printf("\npremi v: ");
    scanf("%c", &c);
    if(c != 'v'){
    printf("\nho detto V!!!");
}
} while (c != 'v');
return 0;
}