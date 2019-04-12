//001
#include <stdio.h>

int isprime(int number) {
    int i;
    for(i = 2; i < number; i++)
        if (number % i == 0)
            return 0;
    return 1;
}

int main() {
    int number = 100, cnt = 0, i;
    for (i = 2; i < number; i++)
        cnt = cnt + isprime(i);
    printf("%d를 넘지 않는 소수는 %d개입니다/ \n", number, cnt);
    return 0;
}

//002
#include <stdio.h>
#define_CRT_SECURE_NO_WARNING

main()
{
    int a,i,j;

    scanf("%d", &a);
    i = a - 1;
    j = 2;
    while(1)
    {
        if(j <= i) {
            if (a % j == 0)
            {
                printf("소수 아님");
                break;
            }
            else
            {
                j++;
            }
        }
        else
        {
            printf("소수");
            break;
        }        
    }
}

//003
#include <stdio.h>

main () {
    int a,i,j;

    scanf("%d", &a);
    i = a -1;
    j = 2;
    while (1) {
        if (j <= i) {
            if (a % j == 0) {
                printf("소수 아님");
                break;
            }
            else {
                j++;
            }
            else {
                printf("소수");
                break;
            }
        }
    }
}

//004
#include <stdio.h>

main () {
    int a,b,big,small,mok,nmg,gcm,lcm;
    scanf("%d %d", &a, &b);
    if ( a >= b) {
        big = a;
        small = b;
    }
    else {
        big = b;
        small = a;
    }
    while (1) {
        mok = big / small;
        nmg = big - mok * small;
        if (nmg == 0) {
            gcm = small;
            lcm = a * b / gcm;
            printf("%d %d", gcm, lcm);
            break;
        }
        big = small;
        small = nmg;
    }
}