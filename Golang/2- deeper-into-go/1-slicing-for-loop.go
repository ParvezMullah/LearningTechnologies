package main

import "fmt"

func main() {
	cards := []string{"Diamond", "Spade"}
	cards = append(cards, "Heart")
	fmt.Println(cards)
	for pos, card := range cards {
		fmt.Println(card)
	}
}
