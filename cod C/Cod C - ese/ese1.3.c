#include <stdio.h>

int main()
{
    int scelta;
    int primo;
    int secondo;
    int risultato;
    float media;

    printf("\nQuale operazione vuoi eseguire?:\n1 Prodotto\n2 Media\n");
    scanf ("%d", &scelta);
    switch(scelta)
    {
        case 1:
        printf ("\nInserisci primo numero: ");
        scanf ("%d", &primo);

        printf ("\nInserisci secondo numero: ");
        scanf ("%d", &secondo);

        risultato = primo * secondo;

        printf ("\n%d * %d = %d\n", primo, secondo, risultato);
        printf ("\nIl prodotto è: %d", risultato);
    break;

    case 2:
    printf ("\nInserisci primo numero: ");
    scanf ("%d", &primo);

    printf ("\nInserisci secondo numero: ");
    scanf ("%d", &secondo);

    media = (primo + secondo) / 2.0;
    
    scanf ("(%d + %d) / 2 = %f", media);
    printf ("\nLa media è: %f");
    break;

    }
    return 0;
}
