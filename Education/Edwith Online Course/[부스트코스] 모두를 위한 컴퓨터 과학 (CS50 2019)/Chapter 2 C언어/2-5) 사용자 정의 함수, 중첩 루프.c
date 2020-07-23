#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("cough\n")
    }
}

//-----------------------------------//

#include <stdio.h>

void cough(int n);

int main(void)
{
    cough(3);
}

void cough(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("cough\n");
    }
}

//-----------------------------------//

#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Positive Integer: ");
    } while (n < 1);
    return n;
}

//------------------------------------------//

#include <stdio.h>

int main(void)
{
    int n;

    do
    {
        printf("Size: ");
        scanf("%d", &n);

    } while (n < 1);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}