package CoreJavaTraining;

public class ifElseLoop {
    public static void main(String[] args) {
        if (4 > 2) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

        for (int i = 0; i < 10; i = i + 2) {
            System.out.println(i);
        }

        while (true) {
            System.out.println("While Loop");
            break;
        }
    }
}