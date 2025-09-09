const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function* data(total_products){

    let l = []
    
    for (let i = 0; i < total_products; i++) {
        l.push(i + 1)
        if (l.length == 10) {
            yield l
            l = []
        }
    }  

    if (l.length > 0) yield l
}


async function proc() {
    
    const dataa = data(31)
    console.log(dataa.next().value)
    console.log(dataa.next().value)
    console.log(dataa.next().value)
    console.log(dataa.next().value)



}

async function main(){
    await proc()
    crw.close()
}

main()