package CoreJavaTraining;

public class StringClassDemo {

    public static void main(String[] args) {
        // String literal
        String a = "Hello";
        // creation object
        String b = new String("java strings");

        System.out.println(a.charAt(2));
        System.out.println(a.indexOf("e"));
        System.out.println(b.substring(3, 7));
        System.out.println(a.concat(b));

        String c = "    spaces are here    ";
        System.out.println(c.trim());
        System.out.println(c.toUpperCase());
        System.out.println(c.split("a"));
    }
}
