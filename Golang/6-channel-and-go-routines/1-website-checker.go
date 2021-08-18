package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
	sites := []string{
		"https://doxper.com",
		"https://google.com/",
		"https://github.com/",
		"https://amazon.com",
		// "https://parvez-close.com",
	}
	c := make(chan string)
	for _, site := range sites {
		go siteChecker(site, c)
	}

	// for i := 0; i < len(sites); i++ {
	// 	fmt.Println(<-c)

	// }

	for l := range c {
		go func() {
			time.Sleep(time.Second * 5)
			siteChecker(l, c)
		}()
	}
}

func siteChecker(site string, c chan string) {
	_, err := http.Get(site)
	if err != nil {
		fmt.Println(site, "is not up!")
		c <- site
		return
	}
	fmt.Println(site, "is up!")
	c <- site
}
