const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()


async function proc(){
    const transactions = [1000, 2000, -500, 3000];

    const USD_transactions = transactions.map((x) => x / 80)
    console.log("Indian Money: ", transactions)
    console.log("USD Equivalent: ", USD_transactions)
}

async function main(){
    await proc()
    crw.close()
}

main()