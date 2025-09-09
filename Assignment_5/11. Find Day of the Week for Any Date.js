const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    let date = new Date( await crw.get("Enter the date:"));
    const days = {
        0:"sunday",
        1:"monday",
        2:"tuesday",
        3:"wednesday",
        4:"thursday",
        5:"friday",
        6:"saturday"
    }

    console.log("Day: " + days[date.getDay()])
}

async function main(){
    await proc()
    crw.close()
}

main()