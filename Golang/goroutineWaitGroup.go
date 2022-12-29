package main

import (
	"fmt"
	"sync"
	"time"
)

func PrintOne() {
	for i := 1; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(i)
	}
	wg.Done()
}

func PrintTwo() {
	for j := -1; j > -5; j-- {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(j)
	}
	wg.Done()
}

var wg sync.WaitGroup

func main() {
	wg.Add(2)
	go PrintOne()
	go PrintTwo()
	wg.Wait()
	// out : -1 1 2 -2 -3 3 4 -4
}
