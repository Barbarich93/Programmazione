#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultato;

    printf ("\nInserisci primo numero: ");
    scanf ("%d", &primo);

    printf ("\nInserisci secondo numero: ");
    scanf ("%d", &secondo);

    risultato = primo * secondo;

    printf ("\n%d * %d = %d\n", primo, secondo, risultato);
    printf ("\nIl prodotto è: %d", risultato);
    
    return 0;
}
