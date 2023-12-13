class Point(
    var x: Int,
    var y: Int
)

enum class Position(
    val x: Int,
    val y: Int
) {
    home(0, 0), away(10, 10);

    fun distance() = x * x + y * y
}

fun main() {
    var p = Point(5, 5)
    println("${p.x} ${p.y}")
    p.x = 10
    p.y = 0
    println("${p.x} ${p.y}")
}