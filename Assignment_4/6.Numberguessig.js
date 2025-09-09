

const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    const randnum = Math.floor(Math.random() * 10);
    let guess = -1;
    do {
        console.log("Enter your guess: ");
        guess = await crw.get();

        if (guess == randnum) {
            console.log("You won!!!");
            return;
        }

        console.log("You guesses wrong. Try again...");
    }while(guess != randnum)
}

proc()