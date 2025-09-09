
const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    let n = Number ( await crw.get("Enter n: ") );

    let ans = Math.abs(n) < 100 ? "Small " : "Large";

    ans += n < 0 ? "Negative " : " Positive";

    ans += n % 2 == 0 ? "Even" : "Odd";

    console.log(ans);
}

proc()