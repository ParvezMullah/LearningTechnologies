package main

import "fmt"

func main() {
	sites := []string{
		"https://github.com/",
		"https://github.com/",
		"https://amazon.com",
		"https://doxper.com"
	}
	for _, site := range sites{
		siteChecker(site)
	}
}

func siteChecker(site string) {
	response, err := http.Get(site)
	if err != nil{
		fmt.Println(site, "is not up!")
		return
	}
	fmt.Println(site, "is up!")
}
