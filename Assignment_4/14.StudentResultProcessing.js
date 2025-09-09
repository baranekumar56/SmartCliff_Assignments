const {consoleRW}= require('./consoleRW.js')
const crw = new consoleRW()

async function proc() {

    let no_of_subjects = Number ( await crw.get("Enter no subjects: "));

    let subjects = {};

    for (let i = 0; i < no_of_subjects; i++) {
        let subject = await crw.get("Enter Subject: ");
        let mark = await crw.get("Enter Mark: ");

        subjects[subject] = mark;
    }

    let average = 0;
    let isFail = false;

    for (subject in subjects) {
        if (subjects[subject] < 35) {
            isFail = true;
            break;
        }
        average += subjects[subject];
    }

    average =  average / subjects.length;

    if (isFail) {
        console.log("Fail");
        return;
    }

    if (average >= 75) {
        console.log("Distinction");
    }else if (average >= 50) {
        console.log("Pass");
    }else {
        console.log("Fail");
    }
    
}

proc()