package CoreJavaTraining;

public class NestedLoop {
    public static void main(String[] args) {
        System.out.println("Nested Loop Basic");
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 5; j++) {
                System.out.println(i * j);
            }
        }
        System.out.println("Nested Loop");

        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
            i++;
            System.out.println("addition");
        }
    }
}