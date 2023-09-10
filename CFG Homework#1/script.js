// Without the event listener the HTML does not load before the JS
// Therefore we need the "DOMContentLoaded" eventListener to be able to change the HTML through JS

document.addEventListener("DOMContentLoaded", function loadScript() {
    let name = prompt("Welcome to Douro Wine Tasting! \n Please let us know your name.")
    document.querySelector("h2").innerHTML = `Hello ${name}, thank you for booking with us.`

// We have 3 types of wines with different prices, on default we have 0 glasses of each wine
    let quantities = {
        White: [0,0,0],
        Red: [0,0,0],
        Rose: [0,0,0] }

    const prices = [1.5, 2, 2.5]; // Prices for each type of wine

    function updatePrice(wineType, wineId) {
    return quantities[wineType][wineId] * prices[wineType][wineId];
    }

    function addGlass(wineType, wineId) {
    quantities[wineType][wineId]++;
    document.getElementById(`wineQuantity${wineType}${wineId + 1}`).innerHTML = quantities[wineType,wineId]; // wineId corresponds to the index, so it starts at 0, therefore I need to add 1
    console.log(quantities[wineType][wineId]); // To make sure that the function is working
    console.log(updatePrice(wineType,wineId)); // To check the calculated price
    }

    function removeGlass(wineType, wineId) {
    if (quantities[wineType][wineId] > 0) {
        quantities[wineType][wineId]--;
        document.getElementById(`wineQuantity${wineType}${wineId + 1}`).innerHTML = quantities[wineType, wineId];
        console.log(quantities[wineType][wineId]); // To make sure that the function is working
        console.log(updatePrice(wineType,wineId)); // To check the calculated price
    }
    }

})