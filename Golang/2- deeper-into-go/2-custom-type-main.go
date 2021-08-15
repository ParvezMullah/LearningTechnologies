package main



func main() {
	cards := newDeck()
	// cardLength := cards.Len()
	// fmt.Println(cardLength)
	// cards.Print()
	// handCards, remainingCards := deal(cards, 3)
	// handCards.Print()
	// remainingCards.Print()
	shuffledCards := cards.shuffle()
	shuffledCards.Print()
}
