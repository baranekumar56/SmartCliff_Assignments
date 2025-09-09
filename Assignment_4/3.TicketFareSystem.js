const {consoleRW} = require('./consoleRW.js');
const crw = new consoleRW()


async function proc() {
    const age = Number( await crw.get("Enter Age: "));
    const day = await crw.get("Enter day: ");

    if (age < 5) {
        if (day == "Sunday") crw.print("Free (50% off applied → still Free)");
        else crw.print("Free\n");
    }else if (age >= 5 && age <= 17) {
        if (day == "Sunday") crw.print("Child Fare (50 % off)");
        else crw.print("Child fare");
    }else if (age >= 18 && age <= 59) {
        if (day == "Sunday") crw.print("Adult Fare (50 % off)");
        else crw.print("Adult fare");
    }else {
        if (day == "Sunday") crw.print("Senior Fare (50 % off)");
        else crw.print("Senior fare");
    }
}

proc()