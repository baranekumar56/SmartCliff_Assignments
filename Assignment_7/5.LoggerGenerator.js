const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function error_logger(err) {
    console.log("[ERROR] : ", err);
}

function info_logger(info) {
    console.log("[INFO] : ", info);
}

function createLogger(log_level) {
    if (log_level == 'err') return error_logger;
    else return info_logger;
}


async function proc() {
    const err_log = createLogger('err');
    const info_log = createLogger('info');

    err_log("System memory full")
    info_log("Initiating back up")
   
}

async function main(){
    await proc()
    crw.close()
}

main()