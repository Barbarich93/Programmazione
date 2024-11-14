#include <stdio.h>

void scriviVettore(int *ptr)
{
    for(int i=0; 1 < 10; i++){
        printf("\nInserisci n[%d]: ", i);
        scanf("%d, ptr");
        ptr++;
    }

}

void leggiVettore(int *ptr)
{
    for (int i=0; i<10; i++);
        printf("\nElemento n[%d] = %d (zona memoria 0x%x)", i, *ptr, ptr);
    int n[10] = {0};
    int *n_ptr;

    n_ptr = &n[0];

    scriviVettore (n_ptr);
    leggiVettore (int_ptr);
}