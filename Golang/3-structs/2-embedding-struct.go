package main

import "fmt"

type contactInfo struct {
	email string
	zip   int
}
type educationalInfo struct {
	course string
	major  string
}
type person struct {
	firstName   string
	lastName    string
	contactInfo contactInfo
	educationalInfo
}

func main() {
	parvez := person{firstName: "Parvez", lastName: "Mullah"}
	contactInfo := contactInfo{email: "p@gmail.com", zip: 400072}
	parvez.contactInfo = contactInfo
	educationalInfo := educationalInfo{course: "MCA", major: "Computer"}
	parvez.educationalInfo = educationalInfo
	fmt.Println(parvez)
}
