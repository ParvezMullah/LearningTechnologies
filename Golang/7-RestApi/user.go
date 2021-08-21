package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var DB *gorm.DB
var err error

const DNS = "root:123456@tcp(127.0.0.1:3307)/mydb?charset=utf8mb4&parseTime=True&loc=Local"

func initializeMigration() {
	DB, err = gorm.Open(mysql.Open(DNS), &gorm.Config{})
	if err != nil {
		fmt.Println("Could not open database", err.Error())
		panic("Cannot connect to DB")
	}
	DB.AutoMigrate(&User{})
}

type User struct {
	gorm.Model
	FirstName string `gorm:"index", json:"first_name"`
	LastName  string `gorm:"index", json:"last_name"`
	lastName  string `json:lastname`
	Email     string `json:email`
}

func GetUsers(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var users []User
	DB.Find(&users)
	json.NewEncoder(w).Encode(users)
}
func GetUser(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var user User
	params := mux.Vars(r)
	id := params["id"]
	DB.Find(&user, id)
	json.NewEncoder(w).Encode(user)
}

func CreateUser(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var user User
	json.NewDecoder(r.Body).Decode((&user))
	DB.Create(&user)
	json.NewEncoder(w).Encode(user)
}

func UpdateUser(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var user User
	params := mux.Vars(r)
	id := params["id"]
	DB.First(&user, id)
	json.NewDecoder(r.Body).Decode((&user))
	DB.Save(&user)
	json.NewEncoder(w).Encode(user)
}

func DeleteUser(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id := params["id"]
	var user User
	DB.Delete(&user, id)
	json.NewEncoder(w).Encode("The User is Deleted Successfully!")
}
