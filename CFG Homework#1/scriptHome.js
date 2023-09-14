// Without this event listener the HTML does not load before the JS
// Therefore we need the "DOMContentLoaded" eventListener to be able to change the HTML through JS

document.addEventListener("DOMContentLoaded", function loadScript1() {
    let name = prompt("Welcome to Douro Wine Tasting! \n Please let us know your name.")
    document.querySelector("h2").innerHTML = `Hello ${name}, thank you for booking with us.`
})
// We have 3 types of wines with different prices, on default we have 0 glasses of each wine
    let quantities = {
        White: [0,0,0],
        Red: [0,0,0],
        Rose: [0,0,0] }

    const prices = [1.5, 2, 2.5]; // Prices for each type of wine

    function addGlass(wineType, wineId) {
        quantities[wineType][wineId]++;
        document.getElementById(`wineQuantity${wineType}${wineId + 1}`).innerHTML = quantities[wineType][wineId]; // wineId corresponds to the index, so it starts at 0, therefore I need to add 1
        console.log(quantities[wineType][wineId]); // To make sure that the function is working
    }

    function removeGlass(wineType, wineId) {
    if (quantities[wineType][wineId] > 0) {
        quantities[wineType][wineId]--;
        document.getElementById(`wineQuantity${wineType}${wineId + 1}`).innerHTML = quantities[wineType][wineId];
        console.log(quantities[wineType][wineId]); // To make sure that the function is working
    }
    }

    function calculateTotalCost() {
        let totalCost = 0;

        // Calculate total cost for White Wine
        for (let i = 0; i < quantities.White.length; i++) {
            totalCost += quantities.White[i] * prices[i];
        }

        // Calculate total cost for Red Wine
        for (let i = 0; i < quantities.Red.length; i++) {
            totalCost += quantities.Red[i] * prices[i];
        }

        // Calculate total cost for Rose Wine
        for (let i = 0; i < quantities.Rose.length; i++) {
            totalCost += quantities.Rose[i] * prices[i];
        }

        return totalCost;
    }

    document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("Next").addEventListener('click', function newPage() {
        const totalCostPage = calculateTotalCost();
        alert(`You have a special offer since you ordered online.\nEnjoy your 10% off!\nYour total cost is ${(totalCostPage*0.9).toFixed(2)}€`);
        // Redirect to new page (Order Page)
        window.location.href = 'order.html'
    })})
