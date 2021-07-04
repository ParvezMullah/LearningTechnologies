/*
Execution context :
    Global context :
        All the objects defined in a file will be in the global context.

    Execution context:
        inside function / sub context will be present in that execution context.
        different functions will have different execution context.

Execution Stack / Calling Stack:
    all the contextes will be push and poped to execution stack.
*/

var myName = "Parry"
function getMyName() {
    return myName
}

function getFriendsSuggestion() {
    debugger
    console.log("getFriendsSuggestion")
    getFriends()
}

function getFriends() {
    debugger
    console.log("getFriends")
    getMostMutualFriends()
}

function getMostMutualFriends() {
    debugger
    console.log("getMostMutualFriends")
}

debugger
getFriendsSuggestion()


/*
Execution Stack/ Calling Stack:

[
    getMostMutualFriends CONTEXT
    getFriends CONTEXT
    getFriendsSuggestion CONTEXT
    GLOBAL CONTEXT(getFriendsSuggestion, getFriends, getMostMutualFriends,getMyName, myName)]
]
*/