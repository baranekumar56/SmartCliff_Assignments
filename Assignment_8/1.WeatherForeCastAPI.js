
const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()


function getWeatherCity(city){
    
    new Promise((resolve, reject) => {
        if (city == 'Chennai') resolve('Sunny in Chennai')
        else reject('City not found')
    }).then((data) => {
        console.log(data)
    }).catch((err) => {
        console.log(err)
    });

}

async function proc(){
    const city = await crw.get("");
    getWeatherCity(city)
}

async function main(){
    await proc()
    crw.close()
}

main()