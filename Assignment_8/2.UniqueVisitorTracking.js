const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()


async function proc(){
    
    let s = new Set();

    // for this example iam gonna get the no of user entries from the usr

    let n = parseInt( await crw.get("Enter the total User Entries:"));
    console.log("Enter entries one by one")

    for (let i = 0; i < n; i++) {
        let user = await crw.get("")

        if (s.has(user)) console.log(`${user} have already appeared`);
        else s.add(user)
    }

    let vals = []
    for (let x of s) vals.push(x)

    console.log(`Unique User id's: ${vals}`)
    console.log(`Unique User Count: ${vals.length}`)

}

async function main(){
    await proc()
    crw.close()
}

main()