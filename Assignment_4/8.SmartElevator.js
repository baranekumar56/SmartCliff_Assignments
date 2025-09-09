
const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function print_status() {

    let floor = Number ( await crw.get("Enter floor number: ") ); 
    let isMaintained = await crw.get("Is the elevator in maintenance: ");

    if (isMaintained == "True") {
        console.log("Maintenance")
        return;
    }

    if (floor == 0) {
        console.log("Lobby");
    }else if (floor >= 1 && floor <= 5) {
        console.log("Go to Office");
    }else if (floor >= 6 && floor <= 9) {
        console.log("Go to Cafeteria");
    }else if (floor == 10) {
        console.log("Enjoy the view");
    }else {
        console.log("Invalid floor")
    }
}

print_status()