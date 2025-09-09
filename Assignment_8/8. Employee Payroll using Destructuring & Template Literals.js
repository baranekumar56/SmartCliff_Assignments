const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()


async function proc(){

    const dat = [ { name: "Alice", salary: 60000, role: "Developer" }, { name: "Bob", salary: 45000 }];

    dat.forEach(record => {
        const {name, salary, role} = record;

        console.log(`Employee: ${name} | Role : ${role === null || role === undefined ? "Not Assigned" : role} | Salary : $${salary}`)
    })


}

async function main(){
    await proc()
    crw.close()
}

main()