
const {consoleRW} = require("./consoleRW.js")
const crw = new consoleRW()

async function proc() {
    let s = await crw.get("Enter the string:");

    let compressed = "";

    for (let i = 0; i < s.length; ) {
        let count = 1;
        let j = i + 1;
        for (; s[j] == s[i]; j++) {
            count++;
        }
        compressed += s[i] + count ;
        i = j;
    }

    console.log(compressed)

}

async function main(){
    await proc()
    crw.close()
}

main()