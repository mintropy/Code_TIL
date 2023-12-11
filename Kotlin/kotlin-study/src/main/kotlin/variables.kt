fun main() {
    val value1 = 20
    val value2: Int = 40 // 타입 지정이 없어도 됨
    // value1 = 60

    var variable1 = "abc" // variable이 사용되지 않고 변경되어 이슈 생성됨
    var variable2 = "xyz"
    variable1 = "test"

    println(value1)
    println(value2)
    println(variable1)
    println(variable2)
}
