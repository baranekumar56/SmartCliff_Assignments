
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
        let date = new Date( await crw.get("Enter date:"));

        // first get the year then the day of the date


        let start_date = new Date();
        start_date.setFullYear(date.getFullYear())
        start_date.setMonth(0)
        start_date.setDate(1)

        // now from that find the date with the first thursday
        let tday = null;
        for (let i = 0; i < 7; i++) {
            if (start_date.getDay() == 5){
                break;
            }
            start_date.setDate(start_date.getDate()+1);
        }

        if (date.getMonth() == 0 && date.getDate() <= start_date.getDate()) {
            console.log(1);
            return;
        }
        let days = 0;
    
            
        while (!(start_date.getFullYear() === date.getFullYear() && start_date.getMonth() === date.getMonth() && start_date.getDate() === date.getDate())) {
            days += 1;
            // console.log(days)
            start_date.setDate(start_date.getDate() + 1)
        }

        console.log(Math.floor(days / 7 + 1));
    
}

async function main(){
    await proc()
    crw.close()
}

main()