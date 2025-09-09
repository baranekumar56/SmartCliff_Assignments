

const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    
    let num1 = await crw.get("Enter num1: ");
    let num2 = await crw.get("Enter num2: ");

    let ans = []

    let m = num1.length, n = num2.length;
    let i = m - 1, j = n - 1;

    let carry = 0;
    let end = Math.max(m, n);

    while (i >= 0 && j >= 0) {
        let t = parseInt(num1[i]) + parseInt(num2[j]) + carry

        carry =parseInt( t / 10)
        ans.unshift(t % 10)
        i--;
        j--;
    }

    while (j >= 0) {
        let t = parseInt(num2[j]) + carry
        carry = parseInt(t/ 10)
        ans.unshift(t % 10);
        j--;
    }

    while (i >= 0) {
        let t  = parseInt(num1[i]) + carry
        carry = parseInt(t / 10)
        ans.unshift(t % 10)
        i--;
    }

    if (carry == 1) ans.unshift(1)

    console.log(ans)
    
}

async function main(){
    await proc()
    crw.close()
}

main()

