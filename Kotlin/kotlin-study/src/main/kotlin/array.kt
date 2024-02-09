fun main() {
    var array = arrayOf(1, 2, 3, 4, 5)

    // 출력
    println("1. 객체를 직접 출력")
    println(array)
    // [Ljava.lang.Integer;@2a84aee7

    println("2. forEach")
    array.forEach { print(it) }
    print("\n")
    // 12334

    println("3. contentToString")
    println(array.contentToString())
    // [1, 2, 3, 4, 5]

    println("4. joinToString")
    println(array.joinToString(" "))
    // 1 2 3 4 5

    var array1 = arrayOfNulls<Int>(10)
    println(array1.contentToString())
    var array2 = IntArray(10)
    println(array2.contentToString())
}