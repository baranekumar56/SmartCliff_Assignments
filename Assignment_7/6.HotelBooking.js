const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

const bookRoom = (type='Standard', nights = 1) => {
    console.log("Room Booked: ", type, " for ", nights, " night(s)");
}

async function proc() {
    bookRoom()
    const type = await crw.get("Enter type: ");
    const nights = await crw.get("Enter nights: ");

    bookRoom(type, nights)
}

async function main(){
    await proc()
    crw.close()
}

main()