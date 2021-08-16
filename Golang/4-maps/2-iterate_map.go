package main

import "fmt"

func main() {
	colors := map[string]string{
		"red":   "red_hex",
		"white": "white_hex",
		"blue":  "blue_hex",
		"green": "green_hex",
	}
	printMap(colors)
}

func printMap(m map[string]string) {
	for color, hex := range m {
		fmt.Println(color, hex)
	}
}
