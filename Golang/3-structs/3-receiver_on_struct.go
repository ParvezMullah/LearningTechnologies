package main

import "fmt"

type person struct {
	firstName string
	lastName  string
}

func (p person) updateFirstName(firstName string) person {
	p.firstName = firstName
	return p
}

func (pointerToPerson *person) updateLastName(lastName string) {
	fmt.Println(*pointerToPerson)
	pointerToPerson.lastName = lastName
}

func main() {
	parvez := person{"Parvez", "Mullah"}
	fmt.Println(parvez)
	parvez = parvez.updateFirstName("Parry")
	fmt.Println(parvez)

	atif := person{"Atif", "Mandal"}
	atif.updateLastName("Mulla")
	fmt.Println(atif)
}
