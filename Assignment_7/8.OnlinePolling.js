const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

function count_votes(...votes) {
    let candidate_w_count = {}

    for (let i = 0; i < votes.length; i++) {
        if (votes[i] in candidate_w_count) candidate_w_count[votes[i]]++;
        else candidate_w_count[votes[i]] = 1;
    }

    for (let c in candidate_w_count) {
        console.log(`${c} has ${candidate_w_count[c]} votes`)
    }
}


async function proc() {
    count_votes("Alice", "Bob", "Alice", "Alice")
}

async function main(){
    await proc()
    crw.close()
}

main()