
const {consoleRW} = require('./consoleRW');
const crw = new consoleRW()

async function proc() {
    let s = await crw.get("");

    let max_len = 1;

    for (let i = 0; i < s.length; i++) {
        let mp = []
        mp[s[i]] = 1;
        let len = 1;
        for (let j = i + 1; j < s.length; j++) {
            if (! (s[j] in mp) ) {
                len += 1;
                mp[s[j]] = 1;
            }else break;
        }
        max_len = Math.max(max_len, len);
    }

    console.log(max_len)

}

async function main(){
    await proc()
    crw.close()
}




main()
console.log("ko");

