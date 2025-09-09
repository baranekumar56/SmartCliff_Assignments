
const readline = require("readline");

class consoleRW {
    constructor(){
        this.rl = readline.createInterface({
                    input: process.stdin,
                    output: process.stdout
                    });
    }

    /**
     * 
     * @param {**writes to console and returns what is written to it} str 
     * @returns returns the data entered in the console
     */
    get(str="") {
        return new Promise(res => this.rl.question(str, res));
    }

    print(str) {
        this.rl.write(str);
    }

    close(){
        this.rl.close();
    }

}

module.exports = {consoleRW}