const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

class NoAnswerError extends Error{
    constructor(message) {
        super(message);
        this.name ="No Answer Error" ;
    }
}

class TimeUpError extends Error{
    constructor(message) {
        super(message);
        this.name = "Time Up Error" ;
    }
}

class InvalidInputError extends Error{
    constructor(message) {
        super(message);
        this.name = "Invalid Input Error";
    }
}

async function proc(){
    const answer = await crw.get("");
    const timeOfSubmission = await crw.get("");

    try {

        if (answer == null) throw new NoAnswerError("No answer selected. Please choose an option");

        for (let i = 0; i < answer.length; i++){
            if (answer[i] < '0' || answer[i] > 9) throw new InvalidInputError("Invalid Input. Answer must be errror").cause
        }

        if (timeOfSubmission == 'timeUp') throw new TimeUpError("Exam time is over. Submission not allowed.");

        console.log("Answer " + answer + " submitted successfully");


    }catch(err) {
        console.log(err)
    }
}

async function main(){
    await proc()
    crw.close()
}

main()