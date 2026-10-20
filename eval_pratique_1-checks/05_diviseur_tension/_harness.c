#include <stdio.h>

float tension_sortie(float vin, float r1, float r2);

int main(void)
{
    printf("%.2f\n", tension_sortie(12.0, 1000.0, 2000.0));
    printf("%.2f\n", tension_sortie(10.0, 1000.0, 1000.0));
    return 0;
}
