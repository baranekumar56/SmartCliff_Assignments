
function addToCart(cart, item) {
    cart.push(item)
}

function calculateTotal(cart) {
    let sum = 0;

    for (let i = 0; i < cart.length; i++){
        sum += cart[i].price * cart[i].quantity;
    }
    return sum;
}

function applyDiscount(total, discountPercentage) {
    return total - (total * ((1 / 100) * discountPercentage));
}

module.exports = {applyDiscount, addToCart, calculateTotal}