

const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    
    let arr1 = (await crw.get("Enter array 1 elements:")).split(" ").map(x => parseInt(x))
    let arr2 = (await crw.get("Enter array 2 elements:")).split(" ").map(x => parseInt(x))

    let arr3 = [...arr1, ...arr2]
   arr3.sort((a, b) => a - b)
   let mid = parseInt(Math.floor(arr3.length / 2));

   if (arr3.length % 2 != 0) console.log(arr3[mid])
    else {  
        console.log((arr3[mid] + arr3[mid - 1]) / 2)
    }
    
}

async function main(){
    await proc()
    crw.close()
}

main()

