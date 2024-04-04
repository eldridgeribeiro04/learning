firstName = prompt("Enter your First name")
lastname  = prompt("Enter your last name:")
age = prompt("Enter your age:")
height = prompt("Enter your height:")
petName = prompt("What is your pets name?")

var count = 0

if (firstName[0] === lastname[0]) {
    count += 1
}

if (age > 20 && age < 30) {
    count += 1
}

if (height <= 170) {
    count += 1
}

if (petName[petName.length - 1] === 'y') {
    count += 1
}

if (count == "4"){
    console.log(count)
    console.log("Agent logged in!")
}
else{
    console.log(count)
    console.log("Sorry, nothing sus")
}

