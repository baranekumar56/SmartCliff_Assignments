
const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()




async function print_status() {
    let status;

    status = Number ( await crw.get("") )

    if (status >= 200 && status < 300 ) {
    console.log("Success")
    }else if (status >= 300 && status < 399) {
        console.log("Redirect")
    }else if (status >= 400 && status < 499) {
        console.log("Client Error")
    }else if (status >= 500 && status < 599 ) {
        console.log("Server Error")
    }else {
        console.log("Invalid Code")
}
}


print_status()