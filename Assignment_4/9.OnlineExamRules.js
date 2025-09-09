
const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()


async function proc() {

    let time_left = Number ( await crw.get("Enter Time left: "));
    let answered = Number ( await crw.get("Enter answered question: "));
    let issubmitted = await crw.get("Enter if already submitted: ");

    if (time_left <= 0) {
        console.log("Submission Failed: No time left");
    }else if (answered < 0)  {
        console.log("Submission Failed: No answers");
    }else if (issubmitted == "False") {
        console.log("Submisson Failed: Already submitted");
    }else {
        console.log("Submission Accepted");
    }
}

proc()