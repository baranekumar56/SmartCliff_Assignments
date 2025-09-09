const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc(){
    let date = new Date( await crw.get("Enter date:"));
    let n = parseInt( await crw.get("Enter N:"));

    const days = {
        0:"sunday",
        1:"monday",
        2:"tuesday",
        3:"wednesday",
        4:"thursday",
        5:"friday",
        6:"saturday"
    }

    while (n--) {
        let day = date.getDay();
        let d = date.getDate();
        if (days[day] == 'friday') {
            date.setDate(d + 3);
        }else date.setDate(d + 1);
    }

    console.log(date.toString())
}

async function main() {
    await proc()
    crw.close()
}

main()