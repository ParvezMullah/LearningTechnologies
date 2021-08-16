package main

import "fmt"

type person struct {
	firstName string
	lastName  string
}

func main() {
	parvez := person{"Parvez", "Mullah"}
	fmt.Println(parvez)
	atif := person{firstName: "Atif", lastName: "Mulla"}
	fmt.Println(atif)
	var aairah person
	fmt.Println(aairah)

	var parry person
	parry.firstName = "Parry"
	parry.lastName = "Rocks"
	fmt.Println((parry))
}
