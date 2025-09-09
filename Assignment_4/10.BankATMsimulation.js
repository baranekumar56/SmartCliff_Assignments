

const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    let balance = 10000;

    while (true) {
        let choice = await crw.get("Enter choice");

        if (choice == 'Deposit') {
            console.log("Enter amount: ");
            balance += Number ( await crw.get());
        }else if (choice == 'Withdraw') {
            console.log("Enter amount to be withdrawn: ");
            let amount = Number ( await crw.get());

            if (amount > balance ) {
                console.log("Insufficient funds...");
            }else balance -= amount;
        }else if (choice == 'CheckBalance'){
            console.log("Balance: " + balance);
        }else {
            console.log("Invalid choice renter...");
        }
    }
}

proc()