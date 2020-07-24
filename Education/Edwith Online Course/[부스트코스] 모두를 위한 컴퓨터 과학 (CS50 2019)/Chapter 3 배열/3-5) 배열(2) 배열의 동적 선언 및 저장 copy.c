#include <stdio.h>

float average(int length, int array[]);

int main(void)
{
    int n;
    printf("Scores:  ");
    scanf("%d", &n);

    int scores[n];
    for (int i = 0; i < n; i++)
    {
        printf("Score %i: ", i + 1);
        scanf("%d", &scores[i]);
    }

    printf("Average: %.1f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float)sum / (float)length;
}
