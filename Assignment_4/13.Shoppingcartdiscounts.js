

const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    let amount = Number ( await crw.get("Enter cart value:"));
    let isPremium = await crw.get("Is user premium: ");
    let day = await crw.get("Enter day:");

    if (amount > 10000) {
        if (day == "Black Friday") console.log("Discount percentage: 50% " );
        else console.log("Discount percentage: 20%");
    }else if (amount > 5000 && amount < 10000) {
        if (day == "Black Friday") console.log("Discount percentage: 50% " );
        else console.log("Discount percentage: 10%");
    }else if (amount < 5000 ) {
        if (isPremium == "Premium") console.log("Discount percentage: 5%");
    }else {
        console.log("No discount applied...");
    }
}

proc()