//001
#include <stdio.h>

main() {
    int i = 250;
    float a = 125.23f;
    float b = 314.1592e+5;
    char c = 'A';
    char dd[] = "Korea";
    printf("10진수i=%d\t8진수i=%o\n",i,i);
    printf("a = %8.2f, b = %e\n", a,b);
    printf(
        "c값은 문자로 %c이고 아스키 코드로 %c이다.\n",c,c);
        printf("%-10s, %10s\n\r", dd, dd);
}

//002
#include <stdio.h>
main() {
    int a,b,c;
    a = 5 % 3;
    a--;
    b = (a++) + 3;
    printf("%d, %d\n", a,b);
    c = (++a) + 3;
    printf("%d, %d, %d\n",a,b,c);
}

//003
#include <stdio.h>
main() {
   int a = 5, b = 7, c,d,e,f;
   c = a & b;
   d = a | b;
   e = a ^ b;
   f = ~b;
   a = a >> 1;
   b = b << 3;
   printf("%d, %d, %d, %d, %d, %d\n",a,b,c,d,e,f);
}

//004
#include<stdio.h>
main()
{
    int a = 2, b = 3, c,d,e;
    c = a > 3 && b > 2;
    d = a > 3 || b > 2;
    e= !c;
    printf("%d, %d, %d\n", c,d,e);
}

//005
#include<stdio.h>
main()
{
    int a = 2, b = 3, c = 4;
    a += 2;
    b *= 2;
    c %= 2;
    printf("%d, %d, %d\n", a,b,c);
}

//006
#include<stdio.h>

main()
{
    int a = 10, b=20, c,d;
    c = a > b ? a : b;
    d = a > b ? a - b : b - a;
    printf("%d, %d\n", c,d);
}

//007
#include<stdio.h>
main()
{
   int a = 2, b = 3, c = 4, d;
   d = a * b + c >= 8 && c / a - b != 0;
   printf("%d\n",d);
}

//008
#include <stdio.h>
main()
{
   int a = 10, even = 0, odd = 0;
   for (int i = 1; i <= a; ++i)
   {
       if (i % 2 == 0)
        even += i;
       else
        odd += i;
   }
   printf("%d, %d\n", even, odd);
}