
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    let m = parseInt(await crw.get("Enter M: "));
    let n = parseInt(await crw.get("Enter N: "));
    console.log("Enter data one by one...");
    let matrix = []
    for (let i = 0; i < m; i++) {
        matrix[i] = []
        for (let j = 0; j < n; j++) {
            matrix[i][j] = await crw.get("");
        }
    }
    let res = []
    
    let r1 = 0, r2 = m - 1, c1 = 0, c2 = n - 1;

    while (r1 <= r2 && c1 <= c2) {
        for (let i = c1; i <= c2; i++) res.push(matrix[r1][i]);

        for (let i = r1+1; i <= r2; i++) res.push(matrix[i][c2]);
        if (r1 < r2)
        for (let i = c2-1; i >= c1 ; --i) res.push(matrix[r2][i]);
        if (c1 < c2)
        for (let i = r2-1; i > r1; --i ) res.push(matrix[i][c1]);

        r1++;
        r2--;
        c1++;
        c2--;
    }
    console.log(res)
    
}

async function main(){
    await proc()
    crw.close()
}

main()

