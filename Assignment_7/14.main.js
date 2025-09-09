

const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()
const {addToCart, applyDiscount, calculateTotal} = require('./14.carUtils')


async function proc(){
    
    let cart = []
    addToCart(cart, {name:"phone", price:100, quantity:3});
    addToCart(cart, {name: "laptop", price:10000, quantity:10})
    let total = calculateTotal(cart);
    console.log("Total: ", total)

    console.log("Discounted Value: ", applyDiscount(total, 10))

}

async function main() {
    await proc()
    crw.close()
}

main()