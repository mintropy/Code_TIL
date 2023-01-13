// package JavaArray;

public class ArrayDemo {
    public static void main(String[] args) {
        int a[] = new int[5];
        for (int i = 0; i < 5; i++) {
            a[i] = i;
            System.out.println(a[i]);
        }

        int b[][] = new int[2][3];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                b[i][j] = i * j;
                System.out.println(b[i][j]);
            }
        }
    }
}