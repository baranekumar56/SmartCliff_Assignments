

const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function summer(){
    console.log("10 % off")
}

function winter(){
    console.log("20 % off");
}

function getDiscountFunction(season) {
    if (season == "summer") return summer;
    else return winter;
}

async function proc(){

    let season =  await crw.get("Enter the season: "); 

    getDiscountFunction(season)();
}

async function main(){
    await proc()
    crw.close()
}

main()