
const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {
    let classs = await crw.get("Enter class: ");
    let baggage = await crw.get("Enter baggage weight: ");
    let isVIP = await crw.get("Is VIP(true or false): ");

    if (isVIP == true) {
        console.log("Priority check-in");
        if (baggage > 30) {
            console.log("+ Extra Baggage fee");
        }
    }else if (classs == "Business") {
        console.log("Priority check-in");
        if (baggage > 30) {
            console.log("+ Extra Baggage fee");
        }
    }else {
        console.log("Normal check-in");
        if (baggage > 30) {
            console.log("+ Extra Baggage fee");
        }
    }
}

proc()