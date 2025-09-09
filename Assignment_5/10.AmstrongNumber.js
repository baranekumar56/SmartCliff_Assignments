
const { consoleRW } = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    let num = (await crw.get(""))

    function bar() {
        console.log("Before");
        return new Promise(r => setTimeout(r, 1000))
            .then(() => console.log("After"));
    }
    console.log(Object.keys(bar()));


    let pow = num.length;

    let s = 0;

    for (let i = 0; i < num.length; i++) {
        s += parseInt(num[i]) ** pow
    }

    if (s.toString() == num) console.log(true)
    else console.log(false)


}

async function main() {
    await proc()
    crw.close()
}

main()

