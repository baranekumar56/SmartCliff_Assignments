

const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {
    const m = Number ( await crw.get("Enter no.of Rows: "));
    const n = Number ( await crw.get("Enter no.of Colums: "));

    const matrix = []

    await crw.print("Enter data one by one...\n")

    for (let i = 0; i < m; i++) {
        matrix[i] = []
        for (let j = 0; j < n; j++) {
            matrix[i][j] = Number( await crw.get());
        }
    }

    let allOk = true;

    checkdata:
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] < 35) {
                console.log("Failed coordinate : " + " ( " + i + " , " + j + " ) ");
                allOk = false;
                break checkdata;
            }
        }
    }
    if (allOk)
    console.log("All ok")
}

proc()