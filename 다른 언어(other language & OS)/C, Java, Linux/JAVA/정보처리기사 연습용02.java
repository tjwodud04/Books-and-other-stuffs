//001
public class Problem {
    public static void main(String[] args) {
        int a,b,c,sum;
        a = b = 1;
        sum = a + b;

        for (int i =3; i <= 5; i++) {
            c = a + b;
            sum += c;
            a = b;
            b = c;
        }
        System.out.println(sum);
    }
}

//002
import java.lang.Math;

public class Test {
    public static void main(String[] args) {
        int p = 2;
        int n = 3;
        while(true) {
            double t = Math.sqrt(n);
            int m = (int)t;
            for (int i = 2; i <= m; i++) {
                int r = n % i;
                if (r == 0)
                    break;
                if (i == m)
                    p = n;
            }
            n++;
            if (n > 100)
                break;
        }
        System.out.printf("%d\n", p);
    }
}

//003
import java.util.Scanner;

public class Section31_Wait {
    public class static void main(String[] args) {
        Scanner scanf = new Scanner(System.in);
        int m, i, j, k, x;
        int data[] = new int[10];
        for (m = 0; m <= 9; m++)
            data[m] = scanf.nextInt();
        for (i = 0; i <= 8; i++) {
            for (j = i + 1; j <= 9; j++) {
                if (data[i] > data[j]) {
                    k = data[i];
                    data[i] = data[j];
                    data[j] = k;
                }
            }
        }
        for (x = 0; x <= 9; x++)
            System.out.printf("%d", data[x]);
        scanf.close();
    }
}

