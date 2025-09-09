
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    let s = await crw.get("Enter the expression:");

    const memo = new Map();

    function dfs(i, open) {
        if (open < 0) return false; 
        if (i === s.length) return open === 0;

        const key = i + "," + open;
        if (memo.has(key)) return memo.get(key);

        let ch = s[i];
        let res = false;

        if (ch === "(") {
            res = dfs(i + 1, open + 1);
        } else if (ch === ")") {
            res = dfs(i + 1, open - 1);
        } else if (ch === "*") {
            res = dfs(i + 1, open)      
               || dfs(i + 1, open + 1) 
               || dfs(i + 1, open - 1); 
        }

        memo.set(key, res);
        return res;
    }

    console.log(dfs(0, 0));
}

async function main(){
    await proc()
    crw.close()
}

main()

