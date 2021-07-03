function Person(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
    this.increaseAge = function () {
        return ++this.age
    }
}

let parry = new Person("Parvez", 25, "Male")
console.log(parry)
console.log(parry.increaseAge())