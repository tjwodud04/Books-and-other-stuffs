//001
#include <stdio.h>

main()
{
    int i,j;
    i = 0;
    j = 0;
    do {
        i++;
        j += i;
    } while (i < 100);
    
    printf("%d %d", i,j);
}

//002
#include <stdio.h>

main()
{
    int i,j;
    i = -1, j = 0;
    do {
        i += 2;
        j += i;
    } while (i < 99);
    printf("%d", j);
}

//003
#include <stdio.h>

main()
{
    int i = 1, k = 1, j = 1;
    do {
        i++;
        j *= i;
        k += j;
    } while ( i < 10);
    printf("%d", k);
}

//004
#include <stdio.h>

main()
{
    int hap, cnt, c;
    int a = 1, b = 1;

    hap = 2;
    cnt = 2;
    while (1)
    {
        c = a + b;
        hap += c;
        cnt++;
        if (cnt < 20) {
            a = b;
            b = c;
        }
        else
        {
            printf("%d", hap);
            break;
        }
    }
}

//005
#include <stdio.h>

main() {
    int a,b,c,sum;
    a = b = 1;
    sum = a + b;
    
    for (int i = 3; i <= 5; i++) {
        c = a +b;
        sum += c;
        a = b;
        b = c;
    }
    printf("%d\n", sum);
}