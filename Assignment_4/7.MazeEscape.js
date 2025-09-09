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

    let i = 0 , j = 0;
    let escaped = false;

    
    outer: while (i < n && j < m) {
    if (matrix[i][j] === 1) {
      break;
    }

    if (i === n - 1 && j === m - 1) {
      escaped = true;
      break outer;
    }

    if (j + 1 < m && matrix[i][j + 1] === 0) {
      j++;
    }
    else if (i + 1 < n && matrix[i + 1][j] === 0) {
      i++;
    }
    else {
      break;
    }
  }

  console.log(escaped ? "Escaped" : "Blocked");
}

proc()