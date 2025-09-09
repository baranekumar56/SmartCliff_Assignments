
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {

    let nums = (await crw.get("Enter the numbers:")).split(" ").map(num => parseInt(num));
    let k = parseInt(await crw.get("Enter K:"));
    let sum = 0;
    let prefMap = {0:1}
    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        
        sum += nums[i]

        // check whether there is a prefix sum before the current index
        if ( (sum - k) in prefMap ) {
            res += prefMap[sum - k]
        }

        if ((sum) in prefMap) {
            prefMap[sum] += 1;
        }else prefMap[sum] = 1;


    
    }
    console.log(res)
}

async function main(){
    await proc()
    crw.close()
}

main()

