#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultato;

    printf ("/Inserisci primo numero: ");
    scanf ("%d, &primo");

    printf ("/nInserisci secondo numero: ");
    scanf ("%d, &secondo");

    risultato = primo + secondo;

    printf("\n%d + %d = %d\n", primo, secondo, risultato);
    printf("\n%d - %d = %d\n", primo, secondo, primo - secondo);
    printf("\n%d * %d = %d\n", primo, secondo, primo * secondo);


    if (secondo != 0)
    {
        printf("\n%d / %d = %d\n", primo, secondo, primo / secondo);
        printf("\n%d / %d ha resto %d\n", primo, secondo, primo % secondo);
    }
    else
    {
        printf("\nHai appena sbloccato una gemma dell' infinito!");
    }


    return 0;
}