package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"time"
)

var stdin = bufio.NewReader(os.Stdin)

func InputIntValue() (int, error) {
	var n int
	_, error := fmt.Scanln(&n)
	if error != nil {
		stdin.ReadString('\n')
	}
	return n, error
}

func main() {
	rand.Seed(time.Now().UnixNano())

	r := rand.Intn(100)
	cnt := 1
	for {
		fmt.Println("숫자를 입력하세요 : ")
		n, err := InputIntValue()
		if err != nil {
			fmt.Println("숫자만 입력하세요.")
		} else {
			if n > r {
				fmt.Println("입력하신 숫자가 더 큽니다.")
			} else if n < r {
				fmt.Println("입력하신 숫자가 더 작습니다")
			} else {
				fmt.Println("숫자를 맞췄습니다. 축하합니다")
				fmt.Println("시도한 횟수 : ", cnt)
				break
			}
			cnt++
		}
	}

}
