package ClassInterface;

// import ClassInterface.Traffic;

public class KoreanTraffic implements Traffic {
    public void green() {
        System.out.println("Go");
    }

    public void red() {
        System.out.println("Stop");
    }

    public void yello() {
        System.out.println("Slow Down");
    }

    public static void main(String[] args) {
        KoreanTraffic kt = new KoreanTraffic();
        kt.green();
        kt.red();
        kt.yello();
    }
}