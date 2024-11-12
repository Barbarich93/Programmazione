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
    
    risultato = primo + secondo;

    printf ("\nLa somma dei due numeri è: %d\n", risultato);

    return 0;
}