package main

import "fmt"

func main() {
	// colors1 := map[string]string{
	// 	"red":  "some_hexa",
	// 	"blue": "some_other_hexa",
	// }
	// fmt.Println(colors1)

	// var colors2 map[string]string
	// fmt.Println(colors2)

	// colors3 := map[string]string{}
	// fmt.Println(colors3)

	colors4 := make(map[string]string)
	fmt.Println(colors4)
	colors4["white"] = "white_hex"
	fmt.Println(colors4)
	delete(colors4, "white")
	fmt.Println(colors4)
	fmt.Println(colors4["white"] == "")
}
