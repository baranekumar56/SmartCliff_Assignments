const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()



async function proc() {
    const personalInfo = {name: "Alice", age: 25};
    const jobInfo = {role: "developer", salary: 60000};

    const res = {...personalInfo, ...jobInfo}
    console.log(res)
}   


async function main(){
    await proc()
    crw.close()
}

main()