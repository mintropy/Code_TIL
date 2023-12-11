fun max1(a: Int, b: Int): Int {
    return if (a > b) a else b
}

fun max2(a: Int, b: Int): Int = if (a > b) a else b

fun main() {
    println(max1(5, 8))
    println(max2(5, 8))
}