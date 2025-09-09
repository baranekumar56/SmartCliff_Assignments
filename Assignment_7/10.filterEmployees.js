const { consoleRW } = require('./consoleRW')
const crw = new consoleRW()

async function proc() {

    let employees = [
        { name: "A", salary: 60000 },
        { name: "B", salary: 40000 },
        { name: "C", salary: 25000 },
        { name: "D", salary: 50000 },
        { name: "E", salary: 30000 }
    ];

    let High_earners = employees.filter(a => a.salary > 50000)
    let Medium_earners = employees.filter(a => a.salary >= 30000 && a.salary <= 50000)
    let Low_earners = employees.filter(a => a.salary < 30000 )

    console.log("High Earners: ", High_earners)
    console.log("Medium Earners: ", Medium_earners)
    console.log("Low Earners: ", Low_earners)

}

async function main() {
    await proc()
    crw.close()
}

main()