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

//005
#include <stdio.h>

main () {
    int b, mok, nmg, i;
    int a[100];
    scanf("%d", &b);
    int c = 0, d = -1;

    while (1) {
        c++;
        if (c <= b) {
            mok = b /c;
            nmg = b - mok * c;
            if (nmg == 0) {
                d++;
                a[d] = c;
            }
        }
        else {
            printf("%d", b);
            for (i = 0; i <= d; i++)
                printf("%d", a[i]);
            break;
        }
    }   
}

//006
#define FIND 7
#include <stdio.h>

main () {
    int i,j,k,L,m;
    int a[10];
    i = -1;

    do {
        i++;
        scanf("%d", &a[i]);
    } while (i < 9);

    j = 9;

    for (k = 0; k <= 9; k++) {
        if (a[k] >= FIND)
            L = a[k] - FIND;
        else
            L = FIND - a[k];
        if (L <= j) {
            j = L;
            m = a[k];
        }
    }
    printf("%d", m);
}

//007
#include <stdio.h>

main () {
    int m,n,x,s;
    int k[10] = {1,2,3,4,7,6,8,9,3,6};
    m = 9;
    n = -1;

    do {
        n++;
        if(k[n] < 5)
            x = 5 - k[n];
        else {
            x = k[n] -5;
        }
        if (m > x) {
            m = x;
            s = k[n];
        }       
    }while (n < 9);
    
    printf("%d", s);
}