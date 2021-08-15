package main

import (
	"fmt"
	"math/rand"
	"time"
)

// create a new type of deck
// which is slicing of string

type deck []string

func newDeck() deck {
	cards := deck{}
	cardSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	cardValues := []string{"Ace", "One", "Two", "Three"}
	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, suit+" of "+value)
		}
	}
	return cards
}

func (d deck) Len() int { return len(d) }

func (d deck) Print() {
	for _, card := range d {
		fmt.Println(card)
	}
}

func deal(d deck, start_pos int) (deck, deck) {
	return d[:start_pos], d[start_pos:]
}

func (d deck) _shuffle() deck {
	// its not actually random all the times
	cardsSize := len(d)
	for pos := range d {
		randomPos := rand.Intn(cardsSize)
		d[randomPos], d[pos] = d[pos], d[randomPos]
	}
	return d
}

func (d deck) shuffle() deck {
	// its actually random all the times
	cardsSize := len(d)
	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)
	for pos := range d {
		randomPos := r.Intn(cardsSize)
		d[randomPos], d[pos] = d[pos], d[randomPos]
	}
	return d
}
