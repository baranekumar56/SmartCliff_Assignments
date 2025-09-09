const { json } = require('stream/consumers')
const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

 async function safeJSONParse(str) {
    try {

        let data = await JSON.parse(str)
        console.log(data)

    }catch(err) {
        console.log("Failed to parse json: ", err)
    }
}

async function proc(){
    
    safeJSONParse(`{"name": "barane","from" "tiruppur"}`);

}

async function main(){
    await proc()
    crw.close()
}

main()