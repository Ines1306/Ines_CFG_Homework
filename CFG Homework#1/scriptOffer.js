document.addEventListener("DOMContentLoaded", function loadScript2() {

// Return a random order number up to 1000
const randomNumbers=[]

for (let i=0; i<1000; i++) {
    const randomNumber = Math.floor(Math.random()*1001)
    randomNumbers.push(randomNumber)
    console.log(randomNumbers) //making sure we have results
}

let randomOrder = randomNumbers[999] // we pick the last random order of the array
console.log(randomOrder) // making sure the randomOrder is working

if (randomOrder > 0) {
    const randomOrderWorking = true // using boolean values
    if (randomOrderWorking) {
        document.querySelector("h6").innerHTML = (`Great! Your order number is ${randomOrder}.
        \n See you in 7 days!`)
    }
}
else {
    document.innerHTML = "Ups! Something went wrong with your order. Please visit our site at another time."
}
})
