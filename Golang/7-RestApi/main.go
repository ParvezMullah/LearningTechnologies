package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func initializeRouter() {
	r := mux.NewRouter()
	r.HandleFunc("/users", GetUsers).Methods("GET")
	r.HandleFunc("/user/{id}", GetUser).Methods("GET")
	r.HandleFunc("/user", CreateUser).Methods("POST")
	r.HandleFunc("/user/{id}", UpdateUser).Methods("PUT")
	r.HandleFunc("/user/{id}", DeleteUser).Methods("DELETE")
	log.Fatal(http.ListenAndServe(":8080", r))
}

func main() {
	initializeMigration()
	initializeRouter()

}
