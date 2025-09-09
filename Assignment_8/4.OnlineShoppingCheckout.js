const { resolve } = require('path');
const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

const handleLogin = (state) => {
    return new Promise((resolve, reject) => {
        if (state == true) {
            resolve("User Have been logged in");
        }else {
            reject("Please Login...");
        }
    })
}

const handlePayment = (state) =>  {
    return new Promise((resolve, reject) => {
        if (state == true) resolve("Payment successfull");
        else reject("Please pay the amount to confirm the order");
    })
}

const handleOrder = (state) => {
    return new Promise((resolve, reject) => {
        if (state == true) resolve("Ordered Successfully...");
        else reject("Failed to confirm the order");
    })
}

async function proc(){
    let logedIn = true;
    let isPayed = true;
    let confirmOrder = false;

    handleLogin(logedIn)
        .then((res) => {
            console.log(res)
            return handlePayment(isPayed)
        }).then((res) => {
            console.log(res)
            return handleOrder(confirmOrder)
        }).then((res) => {
            console.log(res)
        }).catch((err) => {
            console.log(err)
        })
}

async function main(){
    await proc()
    crw.close()
}

main()