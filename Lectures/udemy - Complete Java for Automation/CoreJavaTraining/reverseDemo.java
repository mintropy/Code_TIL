package CoreJavaTraining;

public class reverseDemo {
    public static void main(String[] args) {
        // String s = "some string";
        String s = "madam";

        String t = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            t = t + s.charAt(i);
        }

        System.out.println(s == t);
    }
}
