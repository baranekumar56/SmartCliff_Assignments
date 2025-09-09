const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()


async function proc(){
    
    (function () {
        console.log("Sending Email...");
        setTimeout(()=> console.log("Email Sent successfully"), 3000)
    })();

}

async function main(){
    await proc()
    crw.close()
}

main()