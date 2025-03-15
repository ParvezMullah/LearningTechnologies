/*
go routines: Light weight thread managed by go runtime.
channels : type conduit through which you can send and receive values with the channel operator <-
select: Lets a go routine wait on multiple channels
*/
package main

import (
	"fmt"
	"time"
)

func someFunc(x int) {
	time.Sleep(time.Second)
	fmt.Println(x)
}

func main1() {
	go someFunc(1)
	go someFunc(2)
	go someFunc(3)
	fmt.Println("hi")
	time.Sleep(time.Second * 5)
}

func main3() {
	myChannel := make(chan string)

	go func() {
		myChannel <- "data"
	}()

	msg := <-myChannel

	fmt.Println(msg)

	go func() {
		myChannel <- "other data"
	}()

	otherMsg := <-myChannel

	fmt.Println(otherMsg)
}

func main4() {
	myChannel := make(chan string)

	go func() {
		myChannel <- "myChannel"
	}()

	myAnotherChannel := make(chan string)

	go func() {
		myAnotherChannel <- "myAnotherChannel"
	}()

	select {
	case msgFromChannel := <-myChannel:
		fmt.Println(msgFromChannel)
	case msgFromAnotherChannel := <-myAnotherChannel:
		fmt.Println(msgFromAnotherChannel)
	}
}

/*
1. for-select loop
2. done channel
3. pipelines
*/

// for-select loop
func main5() {
	charChannel := make(chan string, 3)
	chars := []string{"a", "b", "c"}
	for _, s := range chars {
		charChannel <- s
	}
	close(charChannel)
	for s := range charChannel {
		fmt.Println(s)
	}

}

func main6() {
	go func() {
		for {
			select {
			default:
				fmt.Println(("Doing Work!!!"))
			}
		}
	}()
	time.Sleep(time.Second * 10)
}

//done channel
func doWork(done <-chan bool) {
	for {
		select {
		case <-done:
			return
		default:
			fmt.Println("Doing work!")
		}
	}
}

func main7(){
	done:=make(chan bool)
	go doWork(done)
}

//Pineline