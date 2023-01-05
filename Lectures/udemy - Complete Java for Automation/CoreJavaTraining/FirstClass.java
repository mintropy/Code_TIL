package CoreJavaTraining;

public class FirstClass {
    int b = 5;

    // Method
    public void getData() {
        // static int a = 4;
        System.out.println("I am in method");
        // return "Hello";
    }

    public static void main(String[] args) {
        FirstClass fn = new FirstClass();
        fn.getData();
        System.out.println(fn.b);

        SecondClass sn = new SecondClass();
        sn.setData();

        System.out.println("Hello Java!!");
        // System.out.println(a);
    }
}
