package main

import "fmt"

func main() {
	// new()로 생성한 경우 zero value로 초기화
	a := new(int)
	fmt.Println(a)  // 포인터 주소
	fmt.Println(*a) // 값

	// make()로 slice를 생성하면 빈 slice가 생성되지만, 다른 조작이 불가능
	b := new([]int)
	fmt.Println(b)
	fmt.Println(*b)

	// slice 등은 make로 초기화 필요
	c := make([]int, 5)
	fmt.Println(c)
	fmt.Println(len(c))
	fmt.Println(cap(c))
}
