

const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    while (true) {
        let state = 0;
        let counter = 0;
        switch(state) {
            case 0:
                console.log("Green : cars move");
                state = (state + 1) % 3
                counter += 1
                break
            case 1:
                console.log("Yellow : prepare to stop");
                state = (state + 1) % 3
                counter += 1
                break
            case 2:
                console.log("Red: stop");
                state = (state + 1) % 3
                counter += 1
        }

        if (counter *3 == 15) {
            console.log("Stopped after cycles");
            break;
        }
    }
}

proc()