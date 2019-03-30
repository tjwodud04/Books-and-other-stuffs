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

//009
#include <stdio.h>
main()
{
   int a = 15, b;
   if (a > 10)
    b = a - 10;
   b = b + (10 - b);
   printf("%d\n", b);
}

//010
#include <stdio.h>
main()
{
  int a = 10, b = 20, cha;
  if(a > b)
    cha = a - b;
  else
    cha = b - a;
  printf("%d\b", cha);
}

//011
#include<stdio.h>

main()
{
  int jum = 85;
  if(jum >= 90) {
      printf("the grade is A.\n");
  }
  else if(jum >= 80) {
      printf("the grade is B.\n");
  }
  else if(jum >= 70) {
      printf("the grade is C.\n");
  }
  else if(jum >= 60) {
      printf("the grade is D.\n");
  }
  else {
      printf("the grade is F.\n");
  }
}

//012
#include<stdio.h>

main()
{
  int i, hap = 0;
  for (i = 1; i <= 10; ++i)
  {
      hap += i;
  }
  printf("%d, %d \n", i, hap);
}

//013
#include<stdio.h>

main()
{
 int i = 0, hap = 0;
 while (i < 10)
 {
     i++;
     hap += i;
 }
 printf("%d, %d\n", i, hap);
}

//014
#include<stdio.h>

main()
{
 int i = 0, hap = 0;
 do
 {
     i++;
     hap += i;
 } while(i < 10);
 printf("%d, %d\n", i, hap);
}

//015
#include<stdio.h>

main()
{
 int i = 0, hap = 0;
 while (1)
 {
     i++;
     if (i > 10)
        break;
     if (i % 5 == 0)
        continue;
     hap += i;
 }
 printf("%d, %d\n", i, hap);
}

//016
#include<stdio.h>

main()
{
    int a[3][4];
    int i,j,k = 0;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            k++;
            a[i][j] = k;
        }
    }
}

//017
#include<stdio.h>

main()
{
    int a[5];
    int i;
    for (i = 0; i < 5; i++)
        a[i] = i + 10;
    for (i = 0; i < 5; i++)
        printf("%d", a[i]);
}

//018
#include<stdio.h>

main()
{
    int a[5];
    int i;
    int *p;
    
    for (i = 0; i < 5; i++)
        a[i] = i + 10;
    p = a;
    for (i = 0; i < 5; i++)
        printf("%d", *(p+i));
}

//019
#include<stdio.h>

struct sawon
{
    char name[10];
    char jikwi[10];
    int pay;
};

struct sawon data;

main()
{
    printf("name: ");
    scanf("%s", data.name);
    printf("title: ");
    scanf("%s", data.jikwi);
    printf("pay: ");
    scanf("%d", data.pay);
    
    printf("\n\n");
    
    printf("name : %s\n", data.name);
    printf("title : %s\n", data.jikwi);
    printf("pay : %d", data.pay);
}

//020
#include<stdio.h>

int main() {
   int x=10;
   int y=25;
   int z=x+y;
   printf("Sum of x+y = %i", z);
}