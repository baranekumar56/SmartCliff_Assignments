
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    
    let s = await crw.get("");

    // take two pair to create the intervals
    s = s.split(" ").map(x => parseInt(x))
    let intervals = []

    for (let i = 0; i < s.length; i += 2) {
        intervals.push([s[i], s[i+1]])
    }

    intervals.sort((a, b) => a[0] - b[0])
    
    let res = []
    res.push(intervals[0])
    let prev = 0;
    for (let i = 1; i < intervals.length; i++) {
        
        if (res[prev][1] >= intervals[i][0]) {
            // intervals are overlapping we can merge
            res[prev][1] = Math.max(res[prev][1], intervals[i][1]);
        }else {
            res.push(intervals[i]);
            prev++;
        }
    }
    console.log(res)
    
}

async function main(){
    await proc()
    crw.close()
}

main()

