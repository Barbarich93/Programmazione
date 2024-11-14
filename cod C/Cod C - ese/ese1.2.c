#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    float media;

    printf ("\nInserisci primo numero: ");
    scanf ("%d", &primo);

    printf ("\nInserisci secondo numero: ");
    scanf ("%d", &secondo);

    media = (primo + secondo) / 2.0;
    
    scanf ("(%d + %d) / 2 = %f", media);
    printf ("\nLa media è: %f");
    
    return 0;
}