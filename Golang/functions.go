package main

func square(a int, b int) (c int, d int) {
	// <=> func square (a, b int) (c, d int) {}
	c = a * a
	d = b * b
	return // <=> return c, d
}

func main() {
	// function call
	println(square(2, 3)) // 4 9

	// anonymous function
	x, y := func() (int, int) {
		return 3, 4
	}()
	func(a, b int) {
		println(a * b) // 12
	}(x, y)
}
