const {consoleRW} = require('consoleRW.js')
const crw = new consoleRW()

function onSuccess(amount) {
    console.log(`Payment of ${amount} was successful`);
}

function onFailure(){
    console.log("Payment failed. Invalid amount.")
}

function processPayment(amount, onSuccess, onFailure) {
    if (amount > 0) onSuccess();
    else onFailure();
}

async function proc() {

    let amount = await crw.get("Enter amount");

    processPayment(amount, onSuccess, onFailure);

    amount = await crw.get("Enter amount: ");
    processPayment(amount, onSuccess, onFailure);


}

async function main(){
    await proc()
}

main()