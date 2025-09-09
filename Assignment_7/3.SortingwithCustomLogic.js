const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function sortStudents(students, comparator) {
    students.sort(comparator);
}

function sortByMarks(studa, studb){
    return studa.marks - studb.marks;
}

function sortByName(studa, studb) {
    return -studa.name.localeCompare(studb);
}

async function proc() {
    
    let students = [ { name: "Alice", marks: 80 }, { name: "Bob", marks: 60 }];

    console.log("Unsorted Data: ", students);
    sortStudents(students, sortByMarks);
    console.log("Sorted By Marks: ", students);
    sortStudents(students, sortByName);
    console.log("Sorted By Name: ", students)

}

async function main(){
    await proc()
    crw.close()
}

main()