

const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    console.log("Enter words:");

    let words = await crw.get();
    words = words.split(" ")

    console.log("Enter N: ");
    let N = await crw.get();

    for (let i = 0; i < words.length; i++) {
        if (words[i].length >= N) {
            console.log(words[i])
        }
    }

}


proc()