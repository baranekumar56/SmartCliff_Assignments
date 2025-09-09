const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function quizGame() {
    let score = 0;

    return {
        correct: function(){
            score++;
            console.log("Score: ", score);
        },
        wrong: function(){
            score--;
            console.log("Score: ", score);
        }
    }
}

async function proc() {

    let {correct, wrong} = quizGame()

    correct()
    correct()
    correct()

    wrong()
    wrong()


}

async function main(){
    await proc()
    crw.close()
}

main()