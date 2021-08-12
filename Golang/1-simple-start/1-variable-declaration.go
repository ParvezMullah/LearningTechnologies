package main

import "fmt"

func main() {
	var card string = "MyCard"
	var is_female bool = true
	var age int = 25
	height := 1.1
	player := getPlayer()
	fmt.Println(card, is_female, age, height, player)
}

func getPlayer() string {
	return "Parvez"
}
