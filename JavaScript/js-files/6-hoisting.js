/*
        Hoisting
Variable
var :   It will be accessible to entire function scope.
        If we try to access before assignment then value will be undefined.
        if it is assigned in a conditional block and that is not executed then
        it will raise not Defined exception.


named function: 
        It will be hoisted at the top.

anonymous function(function without name and assigned to a variable):
        It will not be hoisted at the top.
*/

console.log("Before myExample: ", myExample("Parvez"))

var myName = "Parry";
function myExample(a) {
    return a;
}


function varScope() {
    console.log("Before : ", belowDefined)
    for (let i = 0; i < 5; i++) {
        if (i % 2 == 0) {
            if (i == 4) {
                lastVal = 4
            }
        }
        if (i == 4) {
            console.log("2 level out of scope lastVal: ", lastVal)
        }
    }
    var belowDefined = "I am defined below."
    console.log("After : ", belowDefined)
    console.log("3 level out of scope lastVal: ", lastVal)
}