package main

import "testing"

func TestNewDeck(t *testing.T) {
	d := NewDeck()
	if len(d) != 16 {
		t.Errorf("expected deck to have 16, but got %d", len(d))
	}
}
