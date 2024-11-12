#include <stdio.h>

int main()
{
    int scelta;
    
    printf("\nBuongiorno, qui il manicomio:\n1 se sei schizzofrenico\n2 se sei paranoico\n3 se hai bassa autostima\n");
    scanf("&d", &scelta);
    switch(scelta);
    {
        case 1:
            printf("\nVorremmo parlare con una altra delle tue personalità");
            break;
        case 2:
            printf("\nTi avviseremo vhe questa chiamata è condivisa con i poteri forti");
            break;
        case 3:
            printf("\nI nostri operatori stanno parlando con persone più importanti di te");
            break;
        default:
        printf("Grazie Artur per averci contattato");
    }
    return 0;
}
