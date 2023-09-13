// 1.
//     Research unshift(), shift() and split()
//     Write a short answer and explain what each one of them does
//     Use unshift(), shift() and split() each in an example with theme 'CGFdegree'

// Answer 1.

// All three are methods.
// unshift() is used with arrays in JS in order to add elements to the beginning of an array.
// When using array.unshift("element1","element2") it returns the array with the new elements.
// Example:
let classSoftware4 = ["Inês","Jax","Sarah","Kayla"]
classSoftware4.unshift("Raneem","Akram")
console.log(classSoftware4) // it returns ['Raneem', 'Akram', 'Inês', 'Jax', 'Sarah', 'Kayla']

// shift() is also used with arrays in JS in order to remove the first element of an array.
// When using array.shift() it returns the first element of the array and the array has now
// one less element (the first one).
// Example:
let assistantInstructor1 = classSoftware4.shift()
console.log(assistantInstructor1) // it returns 'Raneem'
console.log(classSoftware4) // it returns ['Akram', 'Inês', 'Jax', 'Sarah', 'Kayla']

// split() is used with strings in JS in order to transform it into arrays by specifying a delimiter.
// When using string.split("delimiter") it returns the new array with elements from the string
// separated by the delimiter chosen.
// Example:
let instructors = "Anuj, Akram, Fatma, Raneem"
let instructorsArray = instructors.split(", ")
console.log(instructorsArray) // it returns ['Anuj', 'Akram', 'Fatma', 'Raneem']


// 2.
//     Research object methods
//     Write a short answer and explain what they are
//     Use object methods in an example by creating a new object and object methods with the theme
//     'Programming Language'

// Answer 2

// Object methods are functions performed inside objects. In an object method we can
// access object properties using this.property.
// Example:
const programmingLanguage = {
    name: "JavaScript",
    streamClass: "Software4",
    lastJavaScriptClass: "11/09/2023",
    classesInfo: function () {
        return `I have been learning ${this.name} in my class ${this.streamClass}.
        The last class about ${this.name} was on ${this.lastJavaScriptClass}.`
    }
}
console.log(programmingLanguage.classesInfo()) // it returns I have been learning JavaScript
// in my class Software4. The last class about JavaScript was on 11/09/2023.
console.log(programmingLanguage.name); // it returns JavaScript


// 3.
//     Research 3 DOM events onmouseover and two of your choosing
//     Write a short answer and explain what each one of them does

// Answer 3

// The onmouseover DOM event is an event that is triggered when placing the mouse over an element.
// For example changing the color of a button when the mouse hovers over it.
// After moving the mouse to another place in the page the button will stay in the new color.
// The onmouseout DOM event is an event that is triggered when placing the mouse out of an element.
// For example, considering the example of the onmouseover, changing back the color of
// the button when the mouse is out of the button is an example of onmouseout.
// Another DOM event is the onclick, which I used in this homework and we have also talked about it
// in class. This event is triggered when clicking the respective element.
// For example if we use onclick in a button we can set that when we click the button
// an alert will appear to the user (as I did in this homework).

