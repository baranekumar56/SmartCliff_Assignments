
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    let l = await crw.get("Enter the numbers: ");
    let nums = l.split(" ");

    let res = Array(nums.length), pref = Array(nums.length), suff = Array(nums.length);

    let len = nums.length;

    pref[0] = nums[0];
    suff[len - 1] = nums[len - 1]

    for (let i = 1; i < len; i++) {
        pref[i] = pref[i-1] * nums[i];
    }

    for (let i = len - 2; i >= 0; --i) {
        suff[i] = suff[i+1] * nums[i];
    }

    res[0] = suff[1]
    res[len-1] = pref[len-2]

    for (let i = 1; i <  len-1; i++) {
        res[i] = pref[i-1] * suff[i+1];
    }

    console.log(res)

}

async function main(){
    await proc()
    crw.close()
}

main()

