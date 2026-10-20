#include <stdio.h>

int hors_tolerance(float valeur, float min, float max);

int main(void)
{
    printf("%d\n", hors_tolerance(215.0, 220.0, 230.0));
    printf("%d\n", hors_tolerance(225.0, 220.0, 230.0));
    printf("%d\n", hors_tolerance(235.0, 220.0, 230.0));
    printf("%d\n", hors_tolerance(220.0, 220.0, 230.0));
    printf("%d\n", hors_tolerance(230.0, 220.0, 230.0));
    return 0;
}
