#include <stdio.h>

int pgcd(int a, int b);

int main(void)
{
    printf("%d\n", pgcd(48, 18));
    printf("%d\n", pgcd(17, 5));
    printf("%d\n", pgcd(7, 0));
    return 0;
}
