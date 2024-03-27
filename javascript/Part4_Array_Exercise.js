// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
  roster.push(name);
  return roster;
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

function remove(name) {
  const index = roster.indexOf(name);
  console.log(index);
  if (index > -1) {
    roster.splice(index, 1);
  }
  console.log(roster);
}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

var ask = prompt("Do you want to use the web?y/n");


if (ask === "y"){
    var setTrue = false;

    while (!setTrue) {
    var userInput = prompt(
        "Enter a to add name, r to remove name, v to view name and 1 to quit"
    );

    if (userInput.toLowerCase() == "a") {
        var name = prompt("Enter the name you want to add:");
        console.log(addNew(name));
    } else if (userInput.toLowerCase() == "r") {
        removeName = prompt("Enter the name you want to remove");
        console.log(remove(removeName));
    } else if (userInput.toLowerCase() == "v") {
        console.log(roster);
    } else if (userInput.toLowerCase() == "q") {
        console.log("Exiting...");
        break;
    } else {
        alert("Invalid input. Please try again.");
    }
    }
}
alert('Thanks for using the app')