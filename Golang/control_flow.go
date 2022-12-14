package main

func main() {
	x, y := 3, 4

	if n := 2; x%n == 0 {
		println("x is even")
	} else {
		println("x is odd")
	}

	// for loop
	for n := 5; n < 8; n++ {
		println(n)
	}
	// infinite loop
	for {
		if y == 1 {
			break
		}
		println(y)
		y--
	}

	switch x {
	case 1, 2:
		println("x = 1 or 2")
	case 3, 4:
		println("x = 3 or 4")
	default:
		println("x != 1, 2, 3 or 4")
	}
}
