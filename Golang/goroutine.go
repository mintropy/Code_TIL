package main

import (
	"fmt"
	"time"
)

func PrintOne() {
	for i := 1; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(i)
	}
}

func PrintTwo() {
	for j := -1; j > -5; j-- {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(j)
	}
}

func main() {
	go PrintOne()
	go PrintTwo()
	time.Sleep(time.Second)
	// out : -1 1 2 -2 -3 3 4 -4
}
