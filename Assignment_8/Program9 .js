const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function getFlightStatus(flightno){

    return new Promise( async (resolve, reject) => {
        
        await delay(2000)

        if (flightno == 'AI202') resolve("AI202 id On Time");
        else if (flightno == 'AI404') resolve("AI404 is Delayed");
        else {
            reject('Flight not found')
        }
    })
}

async function proc(){
    let flightno = await crw.get("");
    
    try {
        const data = await getFlightStatus(flightno);
        console.log(data)
    }catch(err) {
        console.log(err)
    }
}

async function main(){
    await proc()
    crw.close()
}

main()